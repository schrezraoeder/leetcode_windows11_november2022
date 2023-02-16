class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * n for i in range(m)] 
        dp[-1][-1] = 1 
        # bottom row and rightmost column is always all `1`s 
        for j in range(m):
            dp[j][-1] = 1
        for i in range(n):
            dp[-1][i] = 1 
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1): 
                dp[j][i] = dp[j+1][i] + dp[j][i+1] 
        return dp[0][0] 
                
        
        
        