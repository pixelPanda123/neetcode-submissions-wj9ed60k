class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        i = 0 

        while i < len(nums)-k:
            ans.append(max(nums[i:i+k]))
            i += 1 
        if nums[i:]:
            ans.append(max(nums[i:]))
        return ans
       