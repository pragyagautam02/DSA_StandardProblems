def rMCM(arr,i,j,t):
   if i==j:
      t[i][j]=0
      return t[i][j]
                
   if t[i][j] != -1:
      return t[i][j]
                
   min_ele=10000000000000000000
   for k in range(i,j):
      count = rMCM(arr,i,k,t) + rMCM(arr,k+1,j,t) + (arr[i-1]*arr[k]*arr[j])
      if count<min_ele:
         min_ele=count
            
      t[i][j]=min_ele
      return t[i][j]
        
def MCM(N, arr):
   # code here
   t=[[-1]*(N) for i in range(N)]
   return rMCM(arr,1,N-1,t)

arr=[2,3,4,3,5]
print(MCM(arr,5))
