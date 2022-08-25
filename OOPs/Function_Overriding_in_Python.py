class Add:
    def result(self,a,b):
        print("Addition : ",a+b)

class Multi(Add):
    def result(self,a,b): #here it overrides the method of same name present in Parent class
        super().result(a,b)  #Still if we want to cll it's parent method having same name, use super()
        print("Multiplication : ",a*b)

m = Multi()
m.result(10,20)
    
