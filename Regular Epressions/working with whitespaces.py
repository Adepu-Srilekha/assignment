import re
randstr='''
python is very trending
technology now
machine'''
print(randstr)
regex=re.compile('\n')
randstr=regex.sub('',randstr)
print(randstr)