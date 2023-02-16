# After watching Neetcode solution, again, apparently I went through this one in like August 
# and I did a non-dp solution yesterday 
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = [False] * (len(s) + 1) 
        dp[len(s)] = True 
        
        for i in range(len(s)-1, -1, -1):
            for word in wordDict: 
                if i + len(word) <= len(s): 
                    if s[i:i+len(word)] == word:
                        dp[i] = dp[i + len(word)] 
                if dp[i]:
                    break
        return dp[0] 
                    
        