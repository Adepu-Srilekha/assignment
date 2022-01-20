import time
t=time.localtime(1642658151.4643147)#converts epoch to time_struct
print(t)
date=t.tm_mday
month=t.tm_mon
year=t.tm_year
print('current date is:%d-%d-%d'%(date,month,year))


#to retrieve time from t
hour=t.tm_hour
min=t.tm_min
sec=t.tm_sec
print('the current time is:%d-%d-%d'%(hour,min,sec))