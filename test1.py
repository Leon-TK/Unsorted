# Back depth buffer test?
import math

def Calc(y, z, zFar, yWidth) -> float:
    z = z / zFar
    z = z * 2 - 1
    angle = math.acos(z)
    yd = math.sin(angle)
    y = y + ( y / (yWidth / 2.) * yd)
    return y

print(Calc(0.25, 1.5, 3., 1.))