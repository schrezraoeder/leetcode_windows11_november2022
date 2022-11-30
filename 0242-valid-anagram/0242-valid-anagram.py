# googled for a problem like this on leetcode after spending a few seconds 
# on https://www.udemy.com/course/python-for-data-structures-algorithms-and-interviews/learn/lecture/4309898#overview 

from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s = ''.join(s.split()) # replace s with a version of itself lacking spaces 
        t = ''.join(t.split()) 
        if len(s) != len(t):
            return False 
        q = Counter(s) 
        w = Counter(t) 
        for item in q:
            if q[item] != w[item]:
                return False 
        for item in w:
            if w[item] != q[item]:
                return False 
        return True 
        
        