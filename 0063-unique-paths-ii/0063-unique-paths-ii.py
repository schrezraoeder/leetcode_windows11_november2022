# NOTE: coded up unique paths in a few minutes without consulting any
# outside resources, I last visited this problem in November or so apparently,
# thinking I can code this up in a few minutes as well without consulting any
# outside resources 
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid) # rows 
        n = len(obstacleGrid[0]) # columns guaranteed at least one column so this won't throw an error
        dp = [[0] * n for _ in range(m)] 
        # bottom row & rightmost column are all always `1`s (unless an obstacle in the way):
        for i in range(m-1, -1, -1):
            if not obstacleGrid[i][-1]:
                dp[i][-1] = 1 
            else: 
                break 
        for j in range(n-1, -1, -1):
            if not obstacleGrid[-1][j]:
                dp[-1][j] = 1 
            else: 
                break 
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                if not obstacleGrid[i][j]:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0] 
        
        