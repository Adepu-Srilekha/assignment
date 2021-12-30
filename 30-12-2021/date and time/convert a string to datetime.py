#convert a string to datetime

from datetime import datetime
string1 = datetime.strptime('Dec 30 2021 2:43PM', '%b %d %Y %I:%M%p')
print(string1)