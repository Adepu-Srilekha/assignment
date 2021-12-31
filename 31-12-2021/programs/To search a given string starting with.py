import re
str='hello world'
res=re.search(r'^he',str)
if res:
    print('string starts with he')
else:
    print('string does not start with he')

'''#special characters:
\   escape special character nature
.  Matches any character except new line
^  Matches begining of a string
$   Matches ending of a string'''
