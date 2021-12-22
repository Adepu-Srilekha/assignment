'''super() method:
--It is a built in method which is useful to call the super class constructor or methods from the
sub class
---If the sub class has a constructor then super class constructor is not available to the sub class


super can be used as:

super().__init__() -----------calling super class constructor
super().__init__(arguements) ------------calling super class and passing arguements
super().method() ----------call super class method'''

#creating a super class
class Father:
    def __init__(self,property=0):
        self.property=property
    def display_property(self):
        print('Fathers property:',self.property)

#creating a child class or sub class
class son(Father):
    def __init__(self,property1=0,property=0):
        #if we use super class we cannot access the super class construcor.. so we are passing as the arguement.
        super().__init__(property)
        self.property1=property1
    def display_property(self):
        print('sons property:',self.property1+self.property)
s=son(100.0,200.0)
s.display_property()

