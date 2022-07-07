def matching_subsequence(s,a,n,m):
    i = 0
    j = 0
    s = list(s)
    a = list(a)
    
    while(i < n and j < m ):
        if s[i] == a[j]:
            j += 1
        
        elif s[i] == '?':
            if a[j] != 'a':
                s[i] = 'a'
            else:
                s[i] = 'b'
                
        i += 1
            
    if j < m :
        return ''.join(s)
    else:
        return -1
            
t = int(input())
while(t):
    n , m = list(map(int,input().split()))
    s = input()
    a = input()
    print(matching_subsequence(s,a,n,m))
    
    t -= 1
