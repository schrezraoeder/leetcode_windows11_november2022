class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None] * (amount+1)
        dp[0] = 0 
        for i in range(len(dp)):
            for coin in coins: 
                if (i - coin) >= 0 and (dp[i-coin] is not None): 
                    if dp[i] is not None:
                        dp[i] = min(1 + dp[i-coin], dp[i]) 
                    else:
                        dp[i] = 1 + dp[i-coin]
        print (dp)
        if (dp[-1] is None): return -1
        return dp[-1]
        