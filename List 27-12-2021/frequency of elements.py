# importing the module
import collections

# initializing the list
random_list = ['A', 'A', 'B', 'C', 'B', 'D', 'D', 'A', 'B']

# using Counter to find frequency of elements
frequency = collections.Counter(random_list)

# printing the frequency
print(dict(frequency))
{'A': 3, 'B': 3, 'C': 1, 'D': 2}