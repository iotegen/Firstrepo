#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def isItPolindrom(s):
    return s == "".join(reversed(s))

s = input()

print(isItPolindrom(s))
