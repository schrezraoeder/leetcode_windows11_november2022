from itertools import product 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)] 
        # the first row and first column will always remain 1 for these types of problems with no obstacles 
        for i, j in product (range(1, m), range(1, n)): 
            dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        return dp[-1][-1]
            
            
        