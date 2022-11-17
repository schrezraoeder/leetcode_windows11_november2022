class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for ix, num in enumerate(nums):
            if num <= 0 or num > len(nums):
                nums[ix] = 0 
        print (nums) 
        q = [True] + [False]*len(nums) 
        for num in nums:
            q[num] = True 
        for ix, num in enumerate(q):
            if not num:
                return ix
        return len(nums) + 1 
        