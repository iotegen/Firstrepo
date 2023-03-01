import re

txt = input()

x = re.split(r"[A-Z]", txt)

print(x)