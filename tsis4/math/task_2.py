import math

def trapezoid_area(height, base1, base2):
    area = height*(base1 + base2)/2
    return area

h = int(input("height: "))
a = int(input("base1: "))
b = int(input("base2: "))

print("area:",trapezoid_area(h, a, b))