from collections import Counter 
import numpy as np 

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
#         freq_s = {}
#         freq_t = {} 
        
#         for char in s:
#             if char not in freq_s: 
#                 freq_s[char] = 1
#             else:
#                 freq_s[char] += 1
#         for char in t:
#             if char not in freq_t:
#                 freq_t[char] = 1
#             else:
#                 freq_t[char] += 1 
#         return freq_s == freq_t 
    
        # alternative one-line solution: 
        # return ''.join(sorted(s)) == ''.join(sorted(t)) 
        
        # alternative solution using Counter's: 
        # s = ''.join(s.split()) # replace s with a version of itself lacking spaces 
        # t = ''.join(t.split()) 
        # if len(s) != len(t):
        #     return False 
        # q = Counter(s) 
        # w = Counter(t) 
        # for item in q:
        #     if q[item] != w[item]:
        #         return False 
        # for item in w:
        #     if w[item] != q[item]:
        #         return False 
        # return True 
        
        # alternative solution using count arrays 
        count = [0]*26 
        if len(s) != len(t):
            return False 
        
        for char_s, char_t in zip(s, t): 
            index_s = ord(char_s) - 97 
            count[index_s] += 1 
            index_t = ord(char_t) - 97 
            count[index_t] -= 1 
        return (all(np.array(count) == 0)) 
        
        
        