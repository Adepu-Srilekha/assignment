import datetime
todays=datetime.datetime.now()
y=todays+datetime.timedelta(0,5)
print(todays.time())
print(y.time())