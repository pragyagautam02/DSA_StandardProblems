s = "abczabcdefgabcdmnop" 
count=1
ans=[]

for i in range(len(s)-1):
    if(ord(s[i])==122 and ord(s[i+1])==97):
        count+=1
    else:
       if(abs(ord(s[i])-ord(s[i+1]))==1):
          count+=1
       else:
          ans.append(count)
          count=1
      
ans.append(count)
print(ans)
print(max(ans))
