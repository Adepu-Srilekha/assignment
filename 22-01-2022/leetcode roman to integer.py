num={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
n=0
l=[]
prev=0
value=input("enter the number")
#creating list
for i in value:
    l.append(i)


#counting
for k in l:
    for i ,j in num.items():

        if k==j:
           if prev<i :
              prev = i
              n =i-n
           elif prev >= i :
                prev = i
                n +=i
print(f"from Roman {value} into Integer {n}")