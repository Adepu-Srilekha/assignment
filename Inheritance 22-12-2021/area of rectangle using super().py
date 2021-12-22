#using super we access the super class constructor and method in the sub class itself.

class Square:
    def __init__(self,x):
        self.x=x
    def area(self):
        print('area of a square is:',self.x*self.x)
class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x)
        self.y=y
    def area(self):
        #calling method using super
        super().area()
        print('area of rectangle:',self.x*self.y)

#creating an instance
r=Rectangle(10,20)
r.area()