
'''def minCost(costs,k):
   for i in range(1,len(costs)):
      for j in range(k):
         min_cost = math.inf
         for m in range(k):
            if m!=j:
               min_cost = min(min_cost, costs[i-1][m])
         costs[i][j] += min_cost

   return min(costs[-1])
print(minCost([[17,2,17] ,[16,16,5], [14,3,17] ],3))'''


#O(n*k)+O(k)
import math
def minCost(costs,houses):
   min_val = math.inf
   s_min_val = math.inf

   for i in range(houses):
      curr_val = costs[i][0]
      if curr_val < min_val :
         s_min_val = min_val
         min_val= curr_val
      elif curr_val < s_min_val:
         s_min_val = curr_val

   for i in range(1,len(costs)):
      new_min = math.inf
      new_s_min = math.inf
      for j in range(houses):
         if costs[i-1][j] == min_val:
            costs[i][j] += s_min_val
            
         elif costs[i-1][j] != min_val:
            costs[i][j] += min_val

         if costs[i][j] < new_min:
            new_s_min = new_min
            new_min = costs[i][j]
            
         elif costs[i][j] > new_min and costs[i][j] < new_s_min:
            new_s_min = costs[i][j]

      min_val = new_min
      s_min_val = new_s_min

   return costs[-1][-1]
print(minCost([[17,2,17] ,[16,16,5], [14,3,17] ],3))   
