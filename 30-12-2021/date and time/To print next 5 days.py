import datetime
todays=datetime.datetime.today()
for x in range(0,5):
    print(todays+datetime.timedelta(days=x))