import re

s = input()

pat = r"a.*b"

x = re.search(pat, s)

if x:
    print("yes")
else:
    print("no")