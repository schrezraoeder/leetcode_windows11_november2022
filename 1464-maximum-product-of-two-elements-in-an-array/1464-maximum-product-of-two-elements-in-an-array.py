from collections import namedtuple 

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ix = 0 
        jx = 1 
        if len(nums) == 2: 
            return (nums[ix] - 1) * (nums[jx] - 1) 
        max_two_so_far = namedtuple("Max_Two", "first second") 
        max_two_so_far.first = max(nums[ix], nums[jx]) 
        max_two_so_far.second = min(nums[ix], nums[jx]) 
        max_so_far = max_two_so_far.first 
        for ix, number in enumerate(nums[2:]):
            if number >= max_so_far:
                max_two_so_far.second = max_so_far
                max_so_far = max_two_so_far.first = number 
            elif number >= max_two_so_far.second:
                max_two_so_far.second = number 
        return (max_two_so_far.first - 1) * (max_two_so_far.second - 1) 
                
                       
        
        