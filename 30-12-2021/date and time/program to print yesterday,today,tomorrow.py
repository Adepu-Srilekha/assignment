import datetime

print('today:',datetime.date.today())
today=datetime.date.today()
yesterday=today-datetime.timedelta(days=1)
Tomorrow=today+datetime.timedelta(days=1)
print('yesterday is:',yesterday)
print('Tomorrow :',Tomorrow)