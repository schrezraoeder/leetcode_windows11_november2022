# Naive brute force solution. 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        current_streak = 1 
        best_streak = 1 
        
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        
        nums.sort() # O(n * log[n]) time complexity exceeds the required O(n) time allowed
        
        for ix, num in enumerate(nums[1:]): 
            if num != nums[ix]: 
                if num == nums[ix] + 1: 
                    current_streak += 1 
                    best_streak = max(current_streak, best_streak) 
                else: 
                    current_streak = 1 
        
        return best_streak 
            
        
        
        
        # old presumed correct naive solution, but it timed out 
#         for num in nums: 
#             current_streak = 1 
#             while (num + 1) in nums: 
#                 num += 1 
#                 current_streak += 1 
#                 best_streak = max(current_streak, best_streak) 
        
#         return best_streak 
                
        