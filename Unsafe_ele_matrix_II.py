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
    row=set()
    col=set()
    for i in position:
        row.add(i[0])
        col.add(i[1])
           

    #Step 3
    safe=0 
    for i in range(n):
        for j in range(m):
            if i not in row and j not in col:
                safe+=1

    print(safe)        
