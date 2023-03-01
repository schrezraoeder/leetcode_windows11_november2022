from copy import deepcopy 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def replaceables(counts): 
            if not counts:
                return 0 
            max_so_far = 0 
            for char, count in counts.items():
                if count > max_so_far:
                    max_so_far = count 
                    best = char 
            old_counts = deepcopy(counts) 
            del old_counts[best] 
            summ = 0 
            for char, count in old_counts.items():
                summ += count 
            return summ 
            
                
        best = 0 
        l, r = 0, 0
        counts = {} 
        counts[s[l]] = 1 
        while r < len(s):
            while r < len(s) and replaceables(counts) <= k: 
                if r - l + 1 > best:
                    best = r - l + 1 
                r += 1
                if r < len(s):
                    if s[r] in counts:
                        counts[s[r]] += 1
                    else:
                        counts[s[r]] = 1 
            while replaceables(counts) > k: 
                counts[s[l]] -= 1 
                l += 1 
        return best 
            
            
            
        