# this is the mcoding solution from youtube:
# https://www.youtube.com/watch?v=P9OSkJOVf6U 

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        appearances = [True] + [False] * 10**5
        for num in nums:
            if 0 < num < 10**5+1:
                appearances[num] = True 
        for ix, boolean in enumerate(appearances):
            if not boolean: 
                return ix
        return 10**5+1
            
        