def sieveOfEratosthenes(N):
    arr=[1]*(N+1)
    arr[0]=0
    arr[1]=0
    i=2
    while(i*i<=len(arr)):
        if(arr[i]==1):
            for j in range(i*i,len(arr),i):
                arr[j]=0
        i+=1
    for i in range(len(arr)):
        if(arr[i]==1):
            print(i)

N=int(input("Enter the Range : "))
sieveOfEratosthenes(N)
