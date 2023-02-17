# i remember trying this one once in a Pramp interview. 
# i thought I had it. I didn't. 
# tried it for awhile tonight, gave up & tried coding up 
# the "algorithm" from the solution tab (i.e. translating their
# English / pseudocode algorithm to Python)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def cleanup(p): 
            cleaned_up_pattern = '' 
            ix = 0 
            while ix < len(p): 
                if p[ix] != '*': 
                    cleaned_up_pattern += p[ix] 
                    ix += 1 
                else: 
                    cleaned_up_pattern += p[ix] 
                    while ix < len(p) and p[ix] == '*':
                        ix += 1 
            return cleaned_up_pattern 
        def helper(s, p, dp):
            if (s, p) in dp: 
                return dp[(s, p)] 
            if s == p or p == '*':
                dp[(s, p)] = True 
            elif not p or not s:
                dp[(s, p)] = False 
            elif p[0] == s[0] or p[0] == '?':
                dp[(s, p)] = helper(s[1:], p[1:], dp) 
            elif p[0] == '*':
                dp[(s, p)] = helper(s, p[1:], dp) or helper(s[1:], p, dp) 
            elif p[0] != s[0]:
                dp[(s, p)] = False 
            return dp[(s, p)] 
                
            
        dp = {} # memoization hashmap 
        p = cleanup(p) 
        return helper(s, p, dp) 
                
                        
                
                    
                    
        