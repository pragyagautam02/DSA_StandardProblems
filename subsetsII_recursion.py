class Solution:
    global result
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result=[]
        nums.sort()
        self.fun(0,[],nums)
        self.res=set(tuple(i) for i in self.result)
        return list(self.res)
    
    def fun(self,i,out,input):
        if(i==len(input)):
            self.result.append(out)
            return 
        out1=out[:]  #out1=copy.deepcopy(out)
        out2=out[:]  #out2=copy.deepcopy(out)
        
        out1.append(input[i])
        self.fun(i+1,out1,input)
        self.fun(i+1,out2,input)
