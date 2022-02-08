#To take in the marks of 5 subjects and display the grade.
m1=50
m2=90
m3=80
m4=45
m5=78
sum=m1+m2+m3+m4+m5
avg=sum/5
print(avg)
if avg>=90:
    print('A grade')
elif avg>=80 and avg<90:
    print('Grade B')
elif(avg >= 70 and avg < 80):
    print("Average of 5 marks =", avg, 'Grade =C')
elif(avg >= 60 and avg < 70):
    print("Average of 5 marks =", avg, 'Grade =D')
else:
    print("Average of 5 marks =", avg, 'Grade =E')
