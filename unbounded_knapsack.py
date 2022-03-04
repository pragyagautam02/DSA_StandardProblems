def unbounded_knapsack(wt,val,W,n,dp):
   if n==0 or W==0:
      dp[n][W]=0

   if dp[n][W] != -1:
      return dp[n][W]

   if(wt[n-1] <= W):
      dp[n][W] = max(val[n-1] + unbounded_knapsack(wt,val,W-wt[n-1],n,dp) , unbounded_knapsack(wt,val,W,n-1,dp))
      return dp[n][W]
   else:
      dp[n][W] = unbounded_knapsack(wt,val,W,n-1,dp)
      return dp[n][W]

wt=[1,3,4,5,9]
val=[10,40,50,70,60]
W=8
n=5
dp=[[-1]*(W+1) for i in range(n+1)]

print(unbounded_knapsack(wt,val,W,n,dp))
