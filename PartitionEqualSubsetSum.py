class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.sum=sum(nums)
            
        if self.sum%2==0:
            return self.fun(0,nums,self.sum//2)
        else:
            return False
        
    def fun(self,i,nums,s):
        if(s==0):
            return True
        if(s!=0 and i==len(nums)):
            return False
        
        return self.fun(i+1,nums,s-nums[i]) or self.fun(i+1,nums,s)
        
