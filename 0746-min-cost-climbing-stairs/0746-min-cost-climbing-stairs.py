class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1) 
        dp[0] = cost[0] 
        dp[1] = cost[1] 
        # dp[2] = min(dp[0], dp[1]) + cost[2] 
        # dp[3] = min(dp[1], dp[2]) + cost[3] 
        for x in range(2, len(dp)-1):
            dp[x] = min(dp[x-2], dp[x-1]) + cost[x] 
        dp[-1] = min(dp[-1-2], dp[-1-1])  
        return dp[-1]
        