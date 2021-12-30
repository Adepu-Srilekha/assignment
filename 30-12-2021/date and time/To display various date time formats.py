'''Write a Python script to display the various Date Time formats.

a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week'''

import time
import datetime
print('current date and time',datetime.datetime.now())
print('current year',datetime.date.today().strftime('%y'))
print('month of year',datetime.date.today().strftime('%m'))
print('week number of the year',datetime.date.today().strftime('%W'))
print('week number of the year',datetime.date.today().strftime('%w'))
print('Day of the year',datetime.date.today().strftime('%j'))
print('Day of the month',datetime.date.today().strftime('%d'))
print('Day of week',datetime.date.today().strftime('%A'))
