# NOTE: I had watched 
# https://youtu.be/vMj5_vYCXfA 
class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        stack = []
        m = len(nums) - k 
        p = 0 
        for num in nums: 
            while stack and stack[-1] > num:
                if p < m:
                    stack.pop() 
                    p += 1 
                else:
                    break 
            stack.append(num) 
        return stack[:k]
            
        