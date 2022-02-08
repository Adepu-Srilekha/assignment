#To print all distinct elements in given list

from collections import Counter
list1=['python','geeks','is','geeks','for','is']

#finding frequency of each element using counter
freq=Counter(list1)
#It will give the output in dictionaries based on the count
#print(freq)

for i in freq:
    print(i)
