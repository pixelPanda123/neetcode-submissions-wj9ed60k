class Solution:
    def maxArea(self, heights: List[int]) -> int:
        height = heights
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the area using the shorter of the two heights
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)
            
            # Move the pointer of the shorter height towards the center
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
      