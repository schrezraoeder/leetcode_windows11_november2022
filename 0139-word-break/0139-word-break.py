class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        all_words = set(wordDict)
        #@functools.lru_cache(None) # c.f. https://walkccc.me/LeetCode/problems/0139/ 
        def word_break_recursive(s, cash):
            if len(s) == 0 or s in all_words:
                return True 
            for word in all_words: 
                for i in range(len(s)):
                    if s[:i] in all_words:
                        if s[i:] in cash: 
                            if cash[s[i:]]:
                                return True
                        else:
                            stop = word_break_recursive(s[i:], cash)
                            cash[s[i:]] = stop 
                            #print (self._stop)
                            if stop:
                                return True 
            return False    
        cach_e = {} 
        return word_break_recursive(s, cach_e)
        