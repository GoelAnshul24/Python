from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def show2(self):
        pass
    def show3(self):
        print("I am in show3")
        
class B(A):
    def show1(Self):
        print("I am implementing show1")
    def show3(self):
        print("I am in show3")
    def show3(Self, car):
        return "my car"