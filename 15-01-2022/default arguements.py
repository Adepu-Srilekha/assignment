#default arguments demo
def grocery(item,price=70.00):
    print('item=%s' %item)
    print('price=%.2f'%price)
#call grocery() and pass arguments
grocery(item='oil',price=50.75)
grocery(item='sugar')