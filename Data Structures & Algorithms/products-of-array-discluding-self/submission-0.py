import math 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new = [1] + nums+[1]
        ans = []
        for x in range(1, len(nums)+1):
            ans.append(math.prod(new[:x])*math.prod(new[x+1:]))
        return ans 


        