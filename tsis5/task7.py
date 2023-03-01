import re

snake_case = input()

x = re.split("_",snake_case)
camelCase = ""

for i in x:
    camelCase += i.capitalize()
print(camelCase)