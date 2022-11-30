class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        freq_s = {}
        freq_t = {} 
        
        for char in s:
            if char not in freq_s: 
                freq_s[char] = 1
            else:
                freq_s[char] += 1
        for char in t:
            if char not in freq_t:
                freq_t[char] = 1
            else:
                freq_t[char] += 1 
        return freq_s == freq_t 
        