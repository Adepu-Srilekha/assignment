from datetime import *
#to get date and time
td1=datetime.today()
print(td1)
#to get only date
td2=date.today()
print(td2)

#converting the string format
#strftime=string format of time
str1=td2.strftime('%d,%B,%Y')
print(str1)
#%B--- month full name
#%Y--year with century as decimal number..like 2016..