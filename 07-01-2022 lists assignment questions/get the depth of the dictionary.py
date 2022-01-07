#get the depth of the dictionary:
#creating a dictionary
dict1={'name':'srilekha','company':'MCS','id':'MCS0053'}
print(dict1)
#the prerequisite of this is to create a nested dictionary
#based on flower brackets opened and closed we need to check the depth
dict2={'name':{'a':1,'b':2},'c':{'d':{'e':5,'f':7}}}
print(dict2)
def dict_depth(dic, level = 1):
    str_dic = str(dic)
    counter = 0
    for i in str_dic:
        if i == '{':
            counter += 1
    return(counter)
#dic={'name':{1:{'b':2}}}
#dic={'a':1,'b':{'c':'gee'}}
dic={'name':{'a':1,'b':2},'c':{'d':{'e':{'g':5,'f':7}}}}
result=dict_depth(dic)
print(result)



