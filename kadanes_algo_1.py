import math
def kadanes(arr):
   currsum=0
   maxsum = -(math.inf)
   for i in arr:
      currsum +=i
      if maxsum<=currsum:
         maxsum = currsum
      if currsum < 0:
         currsum = 0
   return maxsum

arr=[-2,3,-1,2]
print(kadanes(arr))
