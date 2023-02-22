import datetime

d1 = datetime.datetime.today()
yd = d1.day - 1
td = d1.day + 1
d2 = datetime.date(d1.year,d1.month,yd)
d3 = datetime.date(d1.year,d1.month,td)
print(d2,d1.strftime("%x"),d3)