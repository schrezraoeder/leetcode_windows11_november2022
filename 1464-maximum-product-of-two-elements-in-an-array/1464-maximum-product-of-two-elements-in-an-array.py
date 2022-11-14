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

# glanced at: 
# https://www.coursera.org/learn/algorithmic-toolbox/lecture/P2hHu/solving-the-maximum-pairwise-product-programming-challenge-improving-the-naive 
# And before watching the video figured I would google for a leetcode problem 
# that sounded similar before watching said video.

# Then as soon as I started coding was thinking I wanted something like what 
# A namedtuple provides so googled something, wound up at: 
# https://realpython.com/python-namedtuple/ 
# read for a few seconds then coded the above up. 
                
        
# I had working solutions to this in early August but I find them harder to read. 
# They looked like this: 
    
# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         i = 0 
#         j = 1 
#         max_so_far = max(nums[i], nums[j])
#         second_place = min(nums[i], nums[j]) 
#         k = 2
#         # max product is stuck at 0 during this while loop 
#         while (k < len(nums)) and (max_so_far <= 2) and (second_place == 1): 
#             if nums[k] > 1: 
#                 second_place = min(nums[k], max_so_far)
#                 max_so_far = max(nums[k], max_so_far) 
#             k += 1 
#         while (k < len(nums)):
#             if nums[k] > second_place: 
#                 second_place = min(nums[k], max_so_far)
#                 max_so_far = max(nums[k], max_so_far) 
#             k += 1 
#         solution = (max_so_far - 1) * (second_place - 1) 
        
#         return solution 
                       
        
        