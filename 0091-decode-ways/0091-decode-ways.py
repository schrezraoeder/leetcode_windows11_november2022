# NOTE: after much struggle with this one, watched the Neetcode solution before coding it up 
class Solution: 
    
    
    
        
        
    def numDecodings(self, s: str) -> int:  
        
        def dfs(pos):
            # if pos >= len(s) - 1:
            #     dp[pos] = 1 
            #     return 1 
            if pos in dp:
                return dp[pos]
            if s[pos] == '0':
                return 0
            # if pos == len(s) - 1:
            #     return 1 
            
            res = dfs(pos+1) 
            if (pos<len(s)-1) and ((s[pos] == '1') or (s[pos] == '2' and s[pos+1] in '0123456')):
                res += dfs(pos+2) 
            dp[pos] = res 
            return res 
        
        dp = {len(s): 1} # base case 
        return dfs(0) 
        
            
        
                
        
        