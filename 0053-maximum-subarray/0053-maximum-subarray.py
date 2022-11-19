# Note to self: i watched the neetcode solution to this 
# easy problem, as I stared at it for awhile and the solution
# i had in my head was more convoluted than I expected was 
# necessary to solve it (it was). 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sub = nums[0] # guaranteed to have non-empty array 
        prospective_max = 0 
        
        for number in nums: 
            if prospective_max < 0: 
                prospective_max = 0 # clip negative prefixes 
            prospective_max += number 
            if prospective_max > max_sub: 
                max_sub = prospective_max 
        
        return max_sub 
            
        