def prime_sieve(number):
    x=max(number)
    arr=[1]*(x+1)
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
            return arr

def waiter(number, q):
    # Write your code here
    prime_list=prime_sieve(number)
    ans=[]
    A=[]
    B=[]
    j=0
    for i in range(len(numbers)):
        if(number[i] % primelist[j])==0:
            B.append(number[i])
        else:
            A.append(number[i])
    B.reverse()
    for i in B:
        ans.append(i) 
        B.pop() 
    j+=1     
    for i in range(len(A)):
        if(A[i] % primelist[j])==0:
            B.append(number[i])
            A.pop()
        else:
            pass
    B.reverse()
    for i in B:
        ans.append(i) 
        B.pop()
