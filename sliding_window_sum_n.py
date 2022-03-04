def subArraySum(arr, n, s):
    sum1=0
    count1=1
    count2=1
    i=0
    while(i<len(arr)):
        if(sum1>s):
            #print(i,count2)
            sum1=sum1 - arr[i-count2]
            count1+=1
        else:
            #print("sum :", sum1 ,i,count2)
            sum1+=arr[i]
            count2+=1
        i+=1
    l=[count1,count2-1]
    return l

"""arr=[1,2,3,7,5]
print(subArraySum(arr, 5, 12))
"""
