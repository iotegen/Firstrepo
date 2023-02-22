import math
import task_1

if __name__== "__main__":
    def area_of_regular_polygon(N, a):
        rad = task_1.degree_to_radian(180/N)
        return round((N*(a**2))/(4*math.tan(rad)), 2)

    n = int(input("Input number of sides: "))
    l = int(input("Input the length of a side: "))

    print("The area of the polygon is:", area_of_regular_polygon(n, l))