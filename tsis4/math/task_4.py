import math

def parallelogram_area(height, lenght):
    return height*lenght

h = int(input("Length of base: "))
l = int(input("Height of parallelogram: "))

print("Area of parallelogram:",parallelogram_area(h, l))
