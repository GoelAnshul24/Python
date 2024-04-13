#Define a class named Shape and its subclass Square. 
# The square class has an init function which takes length as argument. 
# Both classes have an area function which can print the area of shape Where Shape's area is 0 by default

#create an abstract class employee with three methods/functions namely name, e-mail, sap id,
#implement the same class functions with the class professor



import abc

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length):
        self.length = length
        
    def area(self):
        return self.length * self.length

# Testing Shape and Square classes
S1 = Shape()
print("Area of Shape:", S1.area())

S2 = Square(5)
print("Area of Square:", S2.area())

class Employee(abc.ABC):
    @abc.abstractmethod
    def name(self, iname):
        pass
    
    @abc.abstractmethod
    def sapID(self, sapid):
        pass
    
    @abc.abstractmethod
    def email(self, mail):
        pass

class Professor(Employee):
    def name(self, iname):
        self.iname = iname
    
    def sapID(self, sapid):
        self.sapid = sapid
    
    def email(self, mail):
        self.mail = mail
        
# Testing Professor class
p1 = Professor()
p1.name("Harshit")
p1.sapID("500125668")
p1.email("hi@hello.com")

print("Name:", p1.iname)
print("SAP ID:", p1.sapid)
print("Email:", p1.mail)
