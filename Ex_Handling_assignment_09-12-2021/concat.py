print('....using exceptions.......')
def concat(a,b):
    try:
        a=10
        b='python'
        print(a+b)
    except Exception as e:
        print('the error is',e)

concat(10,'python')