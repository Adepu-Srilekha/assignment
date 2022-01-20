#A python program to create a datetime object and then change its contents.
from datetime import *
#creating a datetime object
dt1=datetime(year=2022,month=1,day=20,hour=12,minute=40,second=1)
print(dt1)
dt2=dt1.replace(year=2021,month=5)
print(dt2)