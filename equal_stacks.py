def equalStacks(h1, h2, h3):
    # Write your code here
    h1.reverse()
    h2.reverse()
    h3.reverse()
    
    ch1=[]
    ch1.append(h1[0])
    for i in range(1,len(h1)):
        ch1.append(h1[i]+h1[i-1])
        
    ch2=[]
    ch2.append(h2[0])
    for i in range(1,len(h2)):
        ch2.append(h2[i]+h2[i-1])
        
    ch3=[]
    ch3.append(h3[0])
    for i in range(1,len(h3)):
        ch3.append(h3[i]+h3[i-1])
    
    n1=len(ch1)
    n2=len(ch2)
    n3=len(ch3)
    x=max(n1,n2,n3)
    
    for i in range(x):
        m1=max(ch1)
        m2=max(ch2)
        m3=max(ch3)
        
        z=max(m1,m2,m3)
        
        if z in ch1 and ch2 and ch3 :
            return z
        
        if(z==m1):
            ch1.pop()
            
        elif(z==m2):
            ch2.pop()
        
        else:
            ch3.pop()
            
first_multiple_input = input().rstrip().split()

n1 = int(first_multiple_input[0])
n2 = int(first_multiple_input[1])
n3 = int(first_multiple_input[2])
h1 = list(map(int, input().rstrip().split()))
h2 = list(map(int, input().rstrip().split()))
h3 = list(map(int, input().rstrip().split()))

result = equalStacks(h1, h2, h3)
print(result)

'''
def equalStacks(h1, h2, h3):
    s1, s2, s3 = map(sum, (h1, h2, h3))
    while h1 and h2 and h3:
        m = min(s1, s2, s3)
        while s1 > m: s1 -= h1.pop(0)
        while s2 > m: s2 -= h2.pop(0)
        while s3 > m: s3 -= h3.pop(0)
        if s1 == s2 == s3: return s1
    return 0
'''
