class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums)) 
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)): 
                if nums[j] > nums[i]:
                    dp[i] = max(1, dp[i], 1 + dp[j]) 
        return max(dp)
        