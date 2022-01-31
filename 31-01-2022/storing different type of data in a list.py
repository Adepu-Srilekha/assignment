#A python program to create a list with employee data and then retrieve a particular employee details.
emp=[]
n=int(input('How many employees:'))
for i in range(n):
    id1=int(input('enter Id:'))
    emp.append(id1)
    name1=input('enter the name:')
    emp.append(name1)
    salary1=float(input('Enter salary:'))
    emp.append(salary1)
#display employee details upon taking id
id=int(input('Enter the id of the employee'))
for i in range(len(emp)):
    if id==emp[i]:
        print('id={},Name={},salary={}'.format(id1,name1,salary1))
