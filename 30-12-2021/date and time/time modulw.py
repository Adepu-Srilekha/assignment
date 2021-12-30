'''time()----Returns the number of seconds
ctime()---returns the current date and time
sleep()--- stops execution of a thread for the given function
localtime()-- returns the date and time in time.struct_time format
gmtime()--- returns time.struct_time in UTC format
mktime()--- returns the seconds passed since epoch pas output(inverse of local time)
asctime()-- retuns a string representing the same


struct_time class:
has 9 attributes....starting from the year 0000,...,2019,....9999

tm_mon----month-------------------     1-12
tm_mday---day of the month--------     1-31
tm_hour---------------------------     0-23
tm_min----------------------------     0-59
tm_sec----------------------------      0-61
tm_wday-----week day--------------0-6,where 0 is monday
tm_yday------year day---------------    1-366
tm_isdst---day night saving time---- 1:summer,0:isnot,-1:unknown
'''

import time
print(time.time())
#returns the no.of seconds

#if we want to convert current date and time

#need to pass the seconds as the parameter
print(time.ctime(1640845353.7549555))

#help returns the corresponding information about the function.

print(help(time.time))



print(time.localtime())
#to fetch the no.of seconds

a=time.localtime()
b=time.mktime(a)
print(b)


#to fetch current date and time from local time
c=time.asctime(a)
print(c)
#to show the format codes
print(help(time.strftime))

print(a)
#to get in the formats convenient to us
x=time.strftime('%m/%d/%y')
print(x)

#returning in the struct time format
y='30 December 2021'
s=time.strptime(y,'%d %B %y')
print(s)