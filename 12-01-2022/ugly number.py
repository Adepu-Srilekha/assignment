def ugly_num(num,list1=[2,3,5],flag=False):
    factor_list=[]
    pf_list=[]
    if num in list1 or num == 1:
        flag = True
        return flag
    for i in range(1,num+1):
        if num%i==0:
            factor_list.append(i)
    print(factor_list)
    for ele in factor_list:
        if ele in list1:
            pf_list.append(i)
        else:
            for i in range(2, ele):
                if (ele % i) == 0:
                    pf_list.append(i)
    print(pf_list)
    for ele in pf_list:
        if ele in list1:
            flag=True
        else:
            flag=False
            break

    return flag
num=int(input('enter the number:'))
a=ugly_num(num)
print(a)
