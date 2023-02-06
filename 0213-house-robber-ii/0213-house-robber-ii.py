class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # NOTE: `house_robber_i` is copy-pasted from my solution 
        # to "House Robber", to wit:
        # https://leetcode.com/submissions/detail/892875874/ 
        def house_robber_i(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            if len(nums) <= 1:
                return dp[0] 
            dp[1] = nums[1] 
            if len(nums) == 2:
                return max(nums)
            if len(nums) == 3:
                return max(nums[0] + nums[2], nums[1]) 
            dp[2] = max(nums[0] + nums[2], nums[1]) 
            for x in range(3, len(nums)):
                dp[x] = max(dp[x-2] + nums[x], dp[x-1], dp[x-3] + nums[x])  
            print (dp) 
            return dp[-1] 
        if len(nums) == 1:
            return nums[0] 
        return max(house_robber_i(nums[:-1]), house_robber_i(nums[1:]))
        
        