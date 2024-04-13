class employee:
    Name="harshit"
    Dept="cse"
    def info(self, city):
        print(self.Name, self.Dept, city)

E1=employee()
E2=employee()
city="roorkee"
E1.info(city)
E2.info(city)

class employee:
    def __init__(self, N, D):
        self.N=N
        self.D=D
        print(self.N, self.D)
        
E1=employee("hello", "world")
E2=employee("bye", "world1")