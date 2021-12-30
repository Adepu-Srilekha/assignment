from datetime import *
#creating a datetime object
object1=datetime(year=2021,month=12,day=30,hour=15,minute=30,second=42)
print(object1)
#changing the contents and replacing
object2=object1.replace(year=2000,month=6,day=29)
print(object2)
