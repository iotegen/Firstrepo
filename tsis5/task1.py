#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

text = input()

pat = r"a(b)*"

x = re.search(pat, text)

if x:
    print("valid")
else:
    print("not valid")