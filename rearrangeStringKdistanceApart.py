from collections import deque
from heapq import *
def rearrangeString(s, k):
   freq_map={}
   for i in s:
      freq_map[i]=freq_map.get(i,0)+1
      max_heap=[]

   for i,freq in freq_map.items():
      heappush(max_heap, (-freq,i) )

   q=deque()
   result=[]

   while max_heap:
      freq,ch=heappop(max_heap)
      result.append(ch)
      q.append( (ch,freq+1) )
      if len(q)==k:
         c,f=q.popleft()
      if -f > 0:
         heappush(max_heap,(f,c))
            
   return ''.join(result) if len(result)==len(s) else ""

s = "aabbcc"
rearrangeString(s, 3)
