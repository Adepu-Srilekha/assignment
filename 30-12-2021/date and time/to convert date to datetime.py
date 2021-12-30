#To convert date to datetime

from datetime import date
from datetime import datetime
todays_date = date.today()
print(todays_date)
print(datetime.combine(todays_date, datetime.min.time()))
