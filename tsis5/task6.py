import re

s = input()

x = re.sub(r'\s|,|\.', ":", s)

print(x)