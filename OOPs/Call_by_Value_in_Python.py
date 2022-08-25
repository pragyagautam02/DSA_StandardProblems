#In Python, Call by Value totally depends on the Concept of Immutable datatypes
#Immutable Datatypes - Numbers(int,float,char,bool) and Tuples and Frozen Set

def func(x):
    print("Function recieves : ",x,id(x))

    x = 15
    print("Function updates : ",x,id(x))


x = 10
print("Before : ",x,id(x))

func(x)
print("After : ",x,id(x))
