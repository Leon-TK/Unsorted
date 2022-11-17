#SPDX-FileCopyrightText: 2022 Leonid Tkachenko leon24rus@gmail.com
#SPDX-License-Identifier: MIT License

#Finds common values of 2 lists with delta being different
#Used for music beat/time scales

from datetime import datetime

def getDeltastamps(delta, maxLenght):
    result = []
    nextValue = 0
    index = 0
    while(nextValue < maxLenght):
        result.append(nextValue)
        nextValue = result[index] + delta
        index += 1
    return result

# All args in milisseconds
def findCrossDeltastamps_DEPRECATED(delta1, delta2, lenght) ->list:
    smallerDelta = 0
    biggerDelta = 0

    if delta1 < delta2:
        smallerDelta = delta1
        biggerDelta = delta2
    else:
        smallerDelta = delta2
        biggerDelta = delta1

    bList = getDeltastamps(biggerDelta, lenght)
    sList = getDeltastamps(smallerDelta, lenght)

    result = []
    for elem in sList:
        if elem in bList:
            result.append(elem)

    return result

def findCrossDeltastamps(delta1, delta2, lenght, maxCycles = 100000) ->list:
    delta = findCommonDividable(delta1, delta2, maxCycles)
    result = []
    nextVal = 0
    while(not nextVal > lenght):
        result.append(nextVal)
        nextVal += delta
    return result

def findCommonDividable(delta1, delta2, maxCycles) -> float:

    if delta1 > delta2:
        maxx = delta1
        minn = delta2
    else:
        maxx = delta2
        minn = delta1

    if maxx % minn == 0:
        return maxx
    
    #find first common dividable
    nextt = maxx
    currentCycle = 0
    bOver = currentCycle > maxCycles
    while (nextt % minn != 0 and not bOver):
        nextt += maxx
        currentCycle += 1
    if bOver:
        print("max cycles reached")
    return nextt
    
if __name__ == "__main__":
    beat1 = 60 / 150 * 1000
    beat2 = 60 / 300 * 1000
    lenght = 1000 * 60 * 10
    
    a = datetime.now()
    print(f"Old {findCrossDeltastamps_DEPRECATED(beat1, beat2, lenght)}")
    b = datetime.now()

    c = datetime.now()
    print(f"New {findCrossDeltastamps(beat1, beat2, lenght)}")
    d = datetime.now()

    print(f"Time spent {(b - a).microseconds}")
    print(f"Time spent {(d - c).microseconds}")