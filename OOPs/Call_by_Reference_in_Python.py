#In Python, Call by Reference totally depends on the Concept of Mutable datatypes
#Mutable Datatypes - Lists, Dictionaries, Sets

def func(arr):
    print("Function recieves : ",arr,id(arr))
    arr.append(4)
    print("Function updates : ",arr,id(arr))
    

arr = [1,2,3]
print("Before : ",arr,id(arr))

func(arr)
print("After : ",arr,id(arr))
