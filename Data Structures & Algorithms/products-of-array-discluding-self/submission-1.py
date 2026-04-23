import math 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = [1] + nums+[1]
        ans = []
        for i in range(1,len(new)-1):
            ans.append(math.prod(new[:i])*math.prod(new[i+1:]))
        return ans 


        