class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0 
        r = len(height) - 1 
        current_max_area = -float("inf") 
        while l < r: 
            proposed_max_area = min(height[l], height[r]) * (r - l) 
            if proposed_max_area > current_max_area: 
                current_max_area = proposed_max_area 
            if height[l] < height[r]:
                l += 1 
            else:
                r -= 1 
        return current_max_area 
            
            
        