def sliding_window(arr,k):
    window_sum=0
    for i in range(0,k):
        window_sum += arr[i]
    max_sum=window_sum
    
    for i in range(k,len(arr)):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(window_sum,max_sum)

    print(max_sum)

arr=[1,2,3,4,5,6,7,8,9,10]
k=3
sliding_window(arr,k)     
