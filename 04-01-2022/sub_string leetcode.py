
import itertools
string1='srilekha'
result=[]
print('The original string is:',string1)
for i in range(0,5):
    result.append(list(itertools.combinations(string1,i)))
    print(result)