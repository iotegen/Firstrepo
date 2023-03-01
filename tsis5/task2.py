import re

txt = input()

pat = r'ab{2,3}'

x = re.search(pat, txt)

if x:
    print("Yes")
else:
    print("no")