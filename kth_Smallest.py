from heapq import *
def kthSmallest(nums, k):
   max_heap = []
   for i in range(k):
      heappush(max_heap , -nums[i])
   for j in range(k,len(nums)):
      if -nums[j] > max_heap[0]:
         heappop(max_heap)
         heappush(max_heap , -nums[j])
   return -max_heap[0]

nums=[7,10,4,3,20,15]
print(kthSmallest(nums,3))
