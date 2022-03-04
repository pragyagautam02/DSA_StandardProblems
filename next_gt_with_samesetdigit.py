def next_gt_num(n):
   num=list(map(int,n))
   new_num=sorted(num,reverse=True)
   if(num==new_num):
      return "Not Possible"
   for i in range(len(num)-1,-1,-1):
      if i==-1:
         break
      if num[i] > num[i-1]:
         d=i-1
         break

   min2=min(num[d+1:])
   x=num.index(min2)
   num[d],num[x]=num[x],num[d]

   l2=sorted(num[d+1:])
   l=num[:d+1]+l2

   l_new=list(map(str,l))
   s="".join(l_new)
   return s
     
n=input()
print(next_gt_num(list(n)))
