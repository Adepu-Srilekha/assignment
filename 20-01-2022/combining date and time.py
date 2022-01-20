'''we can combine date class object and time class object using combine()
 syntax:
 d=date(2022,1,20)
 t=time(14,44)
 dt=datetime.combine(d,t)'''


from datetime import *
d=date(2022,1,20)
t=time(15,55)
dt=datetime.combine(d,t)
print(dt)
