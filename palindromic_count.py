def isPalindrome(length,s,count):
   l=[]
   for i in range(len(s)):
      new_str = ""
      j=i
      while(len(new_str)!= length):
         if j+1==len(s):
            break
         new_str += s[j]
         j+=1

      l.append(new_str)
      if(new_str == new_str[::-1]):
         count+=1
   print(l)
   return count
    
n=int(input())
s=input()
m=int(input())
l_set = set(map(int,input().split()))

count=0
for i in l_set:
   count=isPalindrome(i,s,count)
print(count)
