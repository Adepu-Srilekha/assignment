# import the random module
import random
# declare a list
sample_list1 = ['Z', 'Y', 'X', 'W', 'V', 'U']
print("Original LIST1: ")
print(sample_list1)
# first shuffle
random.shuffle(sample_list1)
print("\nAfter the first shuffle of LIST1: ")
print(sample_list1)
# second shuffle
random.shuffle(sample_list1)  
print("\nAfter the second shuffle of LIST1: ")
print(sample_list1)