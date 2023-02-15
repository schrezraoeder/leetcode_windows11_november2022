class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        all_words = set(wordDict)
        
        @functools.lru_cache(None)
        def word_break_recursive(s):
            if len(s) == 0 or s in all_words:
                return True 
            for word in all_words: 
                for i in range(len(s)):
                    if s[:i] in all_words and word_break_recursive(s[i:]):
                        return True 
            return False 
            
            
            
             
        return word_break_recursive(s)
        