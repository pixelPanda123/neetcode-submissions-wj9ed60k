class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*(len(nums))
        n = len(nums)
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    curr =  dp[j]+1
                    dp[i] =max(curr, dp[i])
        return max(dp) 
        

        