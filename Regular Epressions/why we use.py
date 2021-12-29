'''1.suppose we have a logfile..
 and from that we require only date and time ....
 to get that date and time from the logfile we use regular expressions
 2.Imagine you are a sales person and you have lot of email addresses
 and many of them are fake....make use of regular expression
 using the pattern of gmail we can verify th email address
 3.can identify using regular expressions which phone number is right or wrong
 4. using regular expressions we can replace particular string
 5.compatible with all the programming languages
 6.RE is used for describing the search pattern.
  7.for searchin a specific string in a large amount of data.
  8. we can even verify that string has proper format or not
  '''

import re
Nameage='''
Raju is 20 and Rani is 15
Nisha is 24 Nishan is 25'''
#ages expressed in numbers
#Names starting with uppercase letters'''

#making a pattern using regular expressions
ages=re.findall(r'\d{1,3}',Nameage)
names=re.findall(r'[A-Z][a-z]*',Nameage)
agedict={}
x=0
for eachname in names:
    agedict[eachname]=ages[x]
    x+=1
print(agedict)