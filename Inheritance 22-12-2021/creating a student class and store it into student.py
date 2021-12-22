#now we are using student class
from student import Student
#creating instance
s=Student()
#and we are passing the values such as id,marks,etc. from the instance we created
s.setid(1)
s.setname('srilekha')
s.setaddress('Banglore')
s.setmarks(70)


#to retrieve the data from the instance and to display
print('id:',s.getid())
print('name:',s.getname())
print('address:',s.getaddress())
print('marks:',s.getmarks())

