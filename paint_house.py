def minCost(costs):
   for i in range(1,len(costs)):
      costs[i][0] += min(costs[i-1][1],costs[i-1][2])
      costs[i][1] += min(costs[i-1][0],costs[i-1][2])
      costs[i][2] += min(costs[i-1][0],costs[i-1][1])

   return min(costs[-1])

print(minCost([[17,2,17] ,[16,16,5], [14,3,17] ]))
