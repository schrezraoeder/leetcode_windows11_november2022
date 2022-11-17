class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for ix, num in enumerate(nums):
            # replace all num's in nums with 0 if they are 
            # less than 0, equal to 0, or > len(nums) because we do not
            # care about any of these! 
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
        