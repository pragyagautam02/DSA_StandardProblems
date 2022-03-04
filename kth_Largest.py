from heapq import *

def findKthLargest(nums, k):
   min_heap=[]
   n=len(nums)
   for i in range(k):
      heappush(min_heap,nums[i])
        
   for i in range(k,n):
      if (nums[i] > min_heap[0]):
         heappop(min_heap)
         heappush(min_heap,nums[i])
                
   return min_heap[0]

nums=[3,2,3,1,2,4,5,5,6]
print(findKthLargest( nums,4))
