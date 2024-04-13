print(len("Hi"))
print(len([1,2,"hi","0123",2.2]))

class A:
    s=1
    l=int(input("Enter l: "))
    b=int(input("Enter b: "))
    def side(self, s):
        print(self.s*self.s)
        return s
    def area(self, l, b):
        return l*b
    
class B(A):
    def side(self,s):
        print(s*s*s)
    def area(self):
        return "nothing"
    
A1=A()
B1=B()
A1.side(1)