import datetime

d1 = datetime.datetime.today()
day = d1.day - 5 
d2 = datetime.date(d1.year,d1.month,day)
print(d2)
