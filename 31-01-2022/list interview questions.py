#How to concatenate or join two lists in python.
list1=['a','b']
list2=['c','d']
list3=list1+list2
print(list3)


#using append method
list1=['a','b']
list2=['c','d']
for x in list2:
    list1.append(x)
print('list1',list1)


#2.Difference between the list and Tuple.
cars=['bmw','honda','toyota']
#here we can modify in lists
cars[0]='wagonr'
print(cars)


#In tuples..
'''fruits=('apple','banana','mango')
fruits[0]='kiwi'
print('fruits',fruits)'''



#3.How to sort a list in python.
#using sort
number_list=[1,2,7,5,4,9]
print(number_list.sort)
print(number_list)


#using sorted method

number_lista=[1,2,7,5,4,9,10]
number_sorted=sorted(number_lista)
print(number_sorted)


#How to count the number of occurences of specific element in list
class_list=['jack','rahul','garry','rahul','jack']
number_of_jack=class_list.count('jack')
print('number_of_jack',number_of_jack)




#7.how to convert lists to a dictionaries
veg_list=['beetroot','cabbage']
#converting list into dictionary
veg_dictionary = dict.fromkeys(veg_list, "Available")
print( 'veg_dictionary',veg_dictionary)