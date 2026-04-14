from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def binary_search(left: int, target_val: int) -> int:
            low, high = left, len(numbers) - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target_val:
                    return mid
                elif numbers[mid] < target_val:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1  
        
        for i in range(len(numbers)):
            complement = target - numbers[i]
            j = binary_search(i + 1, complement)
            if j != -1:
                return [i + 1, j + 1]  # 1-indexed
