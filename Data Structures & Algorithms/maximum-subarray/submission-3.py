class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm 
        currSum, maxSum = nums[0], nums[0]
        for num in nums[1:]:
            currSum = max(currSum + num, num)
            maxSum = max(currSum, maxSum)
        return maxSum
