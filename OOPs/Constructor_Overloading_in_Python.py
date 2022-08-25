class Constructor_Overloading:
    def __init__(self,x=None,y=None):
        self.x = y
        self.y = y

        print("Constuctor is called")

    def f(self):
        pass

obj1 = Constructor_Overloading(10,20)
obj2 = Constructor_Overloading(10)
