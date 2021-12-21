import Employee, pickle

f = open("Mydata.dat",'wb')

emp = Employee.Employee(108,'sdfg',200)

pickle.dump(emp,f)

f.close()


