class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0]*(n+1)
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1 
        dp[1] = dp[2] = 1 
        for x in range(3, n+1):
            dp[x] = dp[x-3] + dp[x-2] + dp[x-1] 
        return dp[n] 
        