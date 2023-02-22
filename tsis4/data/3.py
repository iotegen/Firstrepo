import datetime 

# d1 = datetime.datetime.now()
# print(d1.strftime("%c"))

d1 = datetime.datetime.today().replace(microsecond=0,)
print(d1)