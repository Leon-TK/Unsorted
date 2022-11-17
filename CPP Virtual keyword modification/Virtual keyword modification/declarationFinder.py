#SPDX-FileCopyrightText: � 2021 Leonid Tkachenko leon24rus@gmail.com
#SPDX-License-Identifier: MIT License

from abc import ABC, abstractmethod
#import logs #TODO: find leotklog

class declarationFinderResult(object):

    def __init__(self) -> None:
        self.beginIndex: int = -1
        self.endIndex: int = -1
        self.signature: str = ''

    def ifFounded(self) -> bool:
        if self.beginIndex == -1 or self.endIndex == -1: return False
        else: return True

class virtualFunctionCppResult(declarationFinderResult):

    def __init__(self) -> None:
        super().__init__()
        self.closeBracetIndex: int  = -1
        self.constEndIndex:    int  = -1
        self.bConst:           bool = False
        self.bPure:            bool = False
        self.bOverride:        bool = False
        self.bFinal:           bool = False
        self.bConstructor:     bool = False
        self.bDestructor:      bool = False
        self.bDefined:         bool = False

class IDeclarationFinder(ABC):

    @abstractmethod
    def findDeclaration() -> declarationFinderResult:
        pass

class virtualFunctionCppFinder(IDeclarationFinder):

    def __init__(self, sIndex, buffer) -> None:
        self.vKeyword = 'virtual '
        self.closeBracet = ')'
        self.endOfDecl = ';'
        self.equal = '='
        self.const = ' const'
        self.sIndex: int = sIndex
        self.buffer: str = buffer

    def findDeclaration(self) -> declarationFinderResult:
        result = virtualFunctionCppResult()

        #find virtual keyword
        sIndex = self.findString(self.vKeyword, self.sIndex, len(self.buffer) - 1, self.buffer)
        if sIndex == -1: 
            result.beginIndex = -1
            result.endIndex = -1
            return result
        else:
            result.beginIndex = sIndex

        bDot = False
        bBracet = False

        #find ';'
        dIndex = self.findString(self.endOfDecl, sIndex, len(self.buffer) - 1, self.buffer)

        #find {
        brIndex = self.findString('{', sIndex, len(self.buffer) - 1, self.buffer)

        #compare ; and {. Which has less index goes as end index
        if dIndex == -1 and brIndex == -1:
            result.beginIndex = -1
            result.endIndex = -1
            return result

        if   dIndex < brIndex and dIndex > -1:
                result.endIndex = dIndex
        elif brIndex > -1:
            bBracet = True
            result.endIndex = brIndex

        #find ')'
        bIndex = self.findString(self.closeBracet, sIndex, len(self.buffer) - 1, self.buffer)
        if bIndex == -1:
            result.beginIndex = -1
            result.endIndex = -1
            return result
        else:
            result.closeBracetIndex = bIndex

        #find "{" between ) and }
        if bBracet:
            clbIndex = self.findString('{', bIndex, brIndex, self.buffer)
            if clbIndex:
                result.bDefined = True
            else:
                result.beginIndex = -1
                result.endIndex = -1
                return result

        if self.isDestructor(self.buffer[result.beginIndex:result.endIndex]):
            result.bDestructor = True
        elif self.isConstructor(self.buffer[result.beginIndex:result.endIndex]): 
            result.bConstructor = True

        # find '='
        if not bBracet:
            eqIndex = self.findString(self.equal, bIndex, result.endIndex, self.buffer)
            if eqIndex > -1:
                result.bPure = True

        # find const
        coIndex = self.buffer.find(self.const, bIndex, result.endIndex)
        if coIndex > -1:
            result.bConst = True
            result.constEndIndex = coIndex + len('const')

        #find override
        if not result.bPure:
            ovIndex = self.buffer.find(' override ', bIndex, result.endIndex)
            if ovIndex > -1:
               result.bOverride = True

        #find final
        if not result.bPure:
            fiIndex = self.buffer.find(' final ', bIndex, result.endIndex)
            if fiIndex > -1:
               result.bFinal = True

        result.signature = self.buffer[sIndex:result.endIndex + 1]

        return result

    def findString(self, vKeyword, startIndex, endIndex, buffer):
        return buffer.find(vKeyword, startIndex, endIndex)

    def isConstructor(self, string):
        
        # check chars between virtual and (
        vKey = "virtual"
        obIndex = string.rfind('(')
        pieStr = string[len(vKey):obIndex]
        #find type in pie

        prevChar = ''
        toggle = 0
        ignoreChars = ['\\r', '\\n', '\\t', ' ', '~']
        for char in pieStr:
            for iChar in ignoreChars:
                if char == iChar:
                    prevChar = char
                    continue
                else:
                    if prevChar in ignoreChars and char not in ignoreChars:
                        toggle += 1
                        prevChar = char
                    else:
                        prevChar = char
                        continue

        if toggle == 2: #function has type. Not contructor
            return False
        if toggle == 1:
            return True
        #logs.errorLog("Function has no type nor name")
        return False # error

    def isDestructor(self, string):
        if self.isConstructor(string):
            if string.rfind('~'):
                return True
            return False
        else:
            return False


