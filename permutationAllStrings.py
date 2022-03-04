l=[]
class Solution:
   def find_permutation(self, S):
      self.solve(list(S),0,len(S)-1)
      return l
   def solve(self,string,left,right):
      global l
      if left==right:
         l.append("".join(string))
      else:
         for i in range(left,right+1):
            string[left],string[i]=string[i],string[left]
            self.solve(string,left+1,right)
            string[left],string[i]=string[i],string[left]

obj=Solution()
ans=obj.find_permutation("ABC")
for i in ans:
   print(i,end=" ")
