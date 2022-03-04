t=int(input())
for i in range(t):
    n,m=list(map(int,input().split()))
    matrix=[]
    for row in range(n):
        matrix.append(list(map(int,input().split())))

    max_ele=matrix[0][0]
    min_ele=matrix[0][0]

    for i in range(n):
        for j in range(m):
            if matrix[i][j]<min_ele:
                min_ele= matrix[i][j]
            if matrix[i][j]>max_ele:
                max_ele= matrix[i][j]
    
    #Step 1
    position=[]
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==min_ele or matrix[i][j]==max_ele:
                position.append([i,j])

    #Step 2
    for i in position:
        row=i[0]
        col=i[1]

        for each_col in range(m):
            matrix[row][each_col]=0

        for each_row in range(n):
            matrix[each_row][col]=0    

    
    #Step 3
    safe=0 
    for i in range(n):
        for j in range(m):
            if matrix[i][j] !=0:
                safe+=1

    print(safe)        
