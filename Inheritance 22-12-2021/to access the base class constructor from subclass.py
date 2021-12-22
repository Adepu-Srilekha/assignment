#creating a super class
class Father:
    def __init__(self):
        self.property=100000
    def display_property(self):
        print('Fathers property:',self.property)

#creating a child class or sub class
class son(Father):
    def __init__(self):
        self.property=20000
    def display_property1(self):
        print('sons property:',self.property)
#creating an instance:
s=son()
s.display_property1()
s1=Father()
s1.display_property()
#whenever we write a constructor in sub class, so the super class constructor is not
# available to the subclass
#in this case only a sub class constructor is accessible from the sub class object
#sub class constructor is replacing the super class constructor-----constructor over riding




#If we write a method with exactly same name as that of super class method,it will overide the
#super classmethod..... method overriding..

