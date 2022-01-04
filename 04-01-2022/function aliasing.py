'''function aliasing:
for the existing function we can give another name,called aliasing'''
def wish(name):
    print('hello',name)

greeting=wish
print(id(greeting))
print(id(wish))

wish('srilekha')
greeting('lekha')