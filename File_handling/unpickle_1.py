import Employee, pickle

f = open("Mydata.dat",'rb')

while True:
    try:
        emp = pickle.load(f)
        emp.display()
    except:
        print("End of file...")
        break
f.close()