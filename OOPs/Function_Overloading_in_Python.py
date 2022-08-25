import math
class Function_Overloading:

    def Area(self,a = None, b = None, c = None):
        if a!=None and b!=None and c!=None:
            print("Area of Triangle : ")
            s = (a+b+c)//2
            area = math.sqrt((s*(s-a)*(s-b)*(s-c)))

        elif a!=None and b!=None:
            print("Area of Rectangle")
            area = a*b

        elif a!=None and type(a)==int:
            print("Area of Square")
            area = a*a

        elif a!=None and type(a)==float:
            print("Area of Circle")
            area = 3.14*a*a

        else:
            print("Provide atleast one argument to calculate Area")
            area = None
            
        return area

obj = Function_Overloading()
print(obj.Area(3,4,5))
print(obj.Area(3,4))
print(obj.Area(3))
print(obj.Area(3.5))

            
            
