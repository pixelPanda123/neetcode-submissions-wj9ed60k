class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1 
        if len(nums)<=2:
            return max(nums)
        n = len(nums)
        arr1 = nums[0:n-1]
        arr2 = nums[1:n]
        # print(arr1)
        # print(arr2)
        def rob_linear(arr):
            m = len(arr)
            if m == 1: return arr[0]
            
            dp = [0] * m
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1]) 

            for i in range(2, m):
                dp[i] = max(dp[i-1], arr[i] + dp[i-2])
            
            return dp[-1]
        return max(rob_linear(arr1), rob_linear(arr2))
        

        """
        :type nums: List[int]
        :rtype: int
        """
        