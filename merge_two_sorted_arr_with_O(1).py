def merge(arr1,arr2,n,m):
    i=n-1
    j=0
    while( i>=0 and j<m):
        if( arr1[i] > arr2[j]):
            arr1[i],arr2[j]=arr2[j],arr1[i]
        else:
            pass
        i-=1
        j+=1
    arr1.sort()
    arr2.sort()

arr1=[1,3,4,6,7]
arr2=[2,5,10]
print(merge(arr1,arr2,n,m))
