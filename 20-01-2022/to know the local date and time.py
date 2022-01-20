'''to know the current date and time, we can also take the help of now() method of datetime
class that belongs to datetime() module.'''
from datetime import *
now=datetime.now()
print(now)
print('Date now:{}/{}/{}'.format(now.day,now.month,now.year))
print('Time now:{}:{}:{}'.format(now.hour,now.minute,now.second))