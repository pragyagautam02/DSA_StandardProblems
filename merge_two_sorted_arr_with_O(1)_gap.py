def next_gap(gap):
    if gap<=1:
        return 0
    else:
        return gap//2 + gap%2
        
def merge(arr1,arr2,n,m):
    gap=n+m
    gap = next_gap(gap)
    while gap>0:
        i=0
        while (i+gap < n):
            if(arr1[i] > arr1[i+gap]):
                arr1[i],arr1[i+gap]=arr1[i+gap],arr1[i]
            i+=1
        if(gap>n):
            j=gap-n
        else:
            j=0
        
        while (j<m and i<n):
            if(arr1[i] > arr2[j]):
                arr1[i],arr2[j]=arr2[j],arr1[i]
            i+=1
            j+=1
            
        if(j<m):
            j=0
        while(j+gap<m):
            if(arr2[j] > arr2[j+gap]):
                arr2[j],arr2[j+gap]=arr2[j+gap],arr2[j]
            j+=1
        gap=next_gap(gap)
        

arr1=[1,2,4,6,7]
arr2=[3,5,10]
merge(arr1,arr2,5,3)
print("1st Array :",arr1)
print("2nd5 Array :",arr2)
