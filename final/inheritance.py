class parent():
    def values(self):
        print("total cost is 5 crore")

class son():
    def values(self):
        print("son has his own property")
        
class daughter():
    def values(self):
        print("daughter is settled abroad")

P1=parent()
P2=son()
P3=daughter()

P1.values()
P2.values()
P3.values()

parent().values()