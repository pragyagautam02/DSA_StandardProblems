def sudoko(matrix,n,m):
   ans=0
   for i in range(n):
      for j in range(m):
         if matrix[i][j]=="s":
            #horizontal
            if((j<=m-4) and (matrix[i][j+1]=="a") and (matrix[i][j+2]=="b") and (matrix[i][j+3]=="a")):
               ans+=1

            #vertical
            if((i<=n-4) and (matrix[i+1][j]=="a") and (matrix[i+2][j]=="b") and (matrix[i+3][j]=="a")):
               ans+=1

            #downwards
            if((i<=n-4 and j<=m-4) and (matrix[i+1][j+1]=="a") and (matrix[i+2][j+2]=="b") and (matrix[i+3][j+3]=="a")):
               ans+=1

            #upwards
            if((i>=3 and j<=m-4) and (matrix[i-1][j+1]=="a") and (matrix[i-2][j+2]=="b") and (matrix[i-3][j+3]=="a")):
               ans+=1
   return ans


n,m=list(map(int,input().split()))

matrix=[]
for i in range(n):
   row=input()
   matrix.append(row)

print(sudoko(matrix,n,m))




