import re
randstr='here is \\python'
print(randstr)
#in tne output we get only one backslash
#in order to solve that prblm we make use of regular expression.
print(re.search(r'\\python',randstr))
#re is raw string and it treats backslashes as special

