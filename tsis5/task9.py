import re

text = input()

x = re.findall(r'[A-Z][a-z]*', text)

res = ""

for i in x:
    res += i + " "
    
print(res)