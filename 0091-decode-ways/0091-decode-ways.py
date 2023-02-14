class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == '0': return 0 
        dp = {len(s):1} # ? 
        for j in range(len(s)-1, -1, -1): 
            if s[j] == '0': 
                dp[j] = 0 
            else:
                dp[j] = dp[j+1] 
            if (j+1 < len(s)) and ((s[j] == '1') or (s[j] == '2' and s[j+1] in '0123456')):
                dp[j] += dp[j+2] 
        return dp[0] 
            
        