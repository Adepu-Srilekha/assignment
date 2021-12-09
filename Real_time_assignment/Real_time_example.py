print('.............welcome to the Supermarket.................')
print('1.View items, 2.Add items,3.purchase items')
items=[]
while True:
    output=input('enter the no.of your choice :')
    if output=='1':
        print('...........1.view items............. ')
        print('The total number of items',len(items))
        while len(items)!=0:
            print('Available items')
            for things in items:
                for key,value in things.items():
                    print(key,':', value)
            break
    elif output=='2':
        print('................2.Add items................')
        print('Adding items')
        item={}
        item['name']=input('enter Item Name:')
        while True:
            try:
                item['quantity']=int(input('enter item quantity:'))
                break
            except ValueError:
                print('enter numeric figure:')
        while True:
            try:
                item['price']=int(input('enter price:'))
                break
            except ValueError:
                print('enter numeric values')
        print('Items successfully added')

        print(items.append(item))

    elif output=='3':
        print('...............3.purchase items..............')
        print('purchasing items')
        pur_item=input('which item do you want to purchase? enter name:')
        for item in items:
            if pur_item.lower()==item['name'].lower():
                if item['quantity']!=0:
                    print('pay',item['price'],'at checkout counter.')
                else:
                    print('item out of stock')

    else:
        break