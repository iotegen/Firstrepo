#Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

s = input()
l = 0
u = 0
for x in s:
    if x.isupper():
        u += 1
    else:
        l += 1
print("number of upper case letters:", u)
print("number of lower case letters:", l)
