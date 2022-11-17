# Some distance field test for shaders?
import math

def getR(N, f):
    return N * f

def getDi(f):
    return 1 / f

def calcRepeat(i, di):
    return math.sqrt(i) * di

def getSum(R, di):
    acc = 0
    i = 0
    for x in range(R):
        acc += calcRepeat(i, di)
        i += di
    return acc

def calcAreaOfSqrX(height, precise):
    di = getDi(precise)
    R = getR(height, precise)
    halfSqrX = getSum(R, di)
    return halfSqrX * 2

print(calcAreaOfSqrX(10, 1000))

    
