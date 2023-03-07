#Write a Python program that invoke square root function after specific milliseconds
import time
import math

def specificSquareRoot(number, mlscnd):
    time.sleep(mlscnd/1000)
    return math.sqrt(n)

n = int(input("write squared number:"))
t = int(input("write milisecond:"))

print(f"Square root of {n} after {t} miliseconds is {specificSquareRoot(n, t)}")