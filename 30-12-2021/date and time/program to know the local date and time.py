from datetime import *
todays=datetime.now()
print(todays)
#printing the date and time in our convenient readable format
print('Date now:{}/{}/{}'.format(todays.day,todays.month,todays.year))
print('Time now:{}:{}:{}'.format(todays.hour,todays.minute,todays.second))