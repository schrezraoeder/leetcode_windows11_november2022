class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max = 1
        current_min = 1
        best_max = -float('inf')
        for num in nums:
            prospects = (num, current_max * num, current_min * num) 
            current_max = max(prospects)
            current_min = min(prospects) 
            if current_max > best_max:
                best_max = current_max 
        return best_max 
        