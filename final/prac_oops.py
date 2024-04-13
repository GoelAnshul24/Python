#wap to use a class to calculate area and parameter of a square
#wap to use a class to calculate area and volume of a cube
#waf tp calculate factorial of a number

class square:
    length=5
    breadth=5
    def area(self):
        print(self.length*self.breadth)
    def parameter(self):
        print(2*self.length+2*self.breadth)
s=square()
s.area()
s.parameter()

class cube:
    length=4
    breadth=4
    height=4
    def area(self):
        print(6*(self.length*self.breadth))
    def volume(self):
        print(self.length*self.breadth*self.height)
c=cube()
c.area()
c.volume()

class factorial:
    def fact(n):
        f=1
        for i in range(1,n+1):
            f=f*i
        print(f)
factorial.fact(5)
            
#wac to generate a multiplication table of n, where n can be any number, also find the factorial, square, cube and sap id+increment using function

class table:
    def __init__(self, n, sap):
        self.n = n
        self.sap = sap
        for i in range(1, 11):
            print(self.n,"X",i,"=",i*self.n,sap+i-1)
    
t1 = table(2, 500125668)