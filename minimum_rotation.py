def minimum_rotation(s):
   if(s==s[::-1]):
      return 1
   
   else:
      return len(s)
  
s=input()
print(minimum_rotation(s))
