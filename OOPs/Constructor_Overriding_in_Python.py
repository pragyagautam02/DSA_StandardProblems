class A():
    def __init__(self,a,b):
        self.a = a
        self.b = b

        print("Inside Parent Class Constructor : ")
        print(self.a * self.b)

class B(A):
    def __init__(self,a,b): #Child class constructor overriding Parent class Constructor
        super().__init__(a,b) #still if we want to have properties of PArent class Constructor
        self.a = a
        self.b = b

        print("Inside Child Class Constructor : ")
        print(self.a + self.b)

obj = B(10,20)
