import re

txt = input()
l = list()
c = re.findall('[A-Z][a-z]*', txt)
for i in c:
    l.append(i.lower())
r = "_".join(l)
print(r)