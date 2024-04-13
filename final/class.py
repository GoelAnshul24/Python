class A:
    name= "harshit"
    sapID= 500125668
    
    def __init__(self, x, y):
        self.name=x
        self.sapID=y
        
        print("I am inside the init of class A")
        
    def showA(self):
        print("inside show of A")
        
    def attrib(self):
        print(self.name, self.sapID)  #name and sapID has been made globally
        
class B(A):
    def __init__(self):
        print("I am inside an inner class")
    def showB(self):
        print("inside the show of B")
        
class C(B):   #we can also access 'class A' by wiriting "class C(A,B)"
    pass      #used for creating empty class
    
a1=A("harshit", 500125668)

b1=B()
b1.attrib()

c1=C()
c1.showB()