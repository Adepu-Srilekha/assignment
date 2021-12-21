#pickle in python:
'''Pickle is a process of converting a class object into a byte stream so that it can be stored into
a file


If we want to store some structured data in the files such as:
emp id(int)
name(string)
salary (float)

To store such data we need to create a class employee with the instance variables.'''

class Employee:
    def __init__(self,empid,name,salary):
        self.empid=empid
        self.name=name
        self.salary=salary
    def display(self):
        print('{} {} {}'.format(self.empid,self.name,self.salary) )






