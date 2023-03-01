import re

pat = r"[A-Z][a-z]+"

text = input()

x = re.findall(pat, text)

print(x)