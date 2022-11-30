# Note: I watched the neetcode solution video first 

class Solution(object):
    def count_from_position(self, s, l, r, count):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1 
            l -= 1 
            r += 1 
        return count 
    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 # count of number of palindromic substrings found so far 
        for i in range(len(s)): 
            # count odd-lengthed palindromic substrings 
            l = r = i 
            count = self.count_from_position(s, l, r, count) 
            # while l >= 0 and r < len(s) and s[l] == s[r]:
            #     count += 1 
            #     l -= 1 
            #     r += 1 
            l, r = i, i + 1 
            count = self.count_from_position(s, l, r, count)
            # while l >= 0 and r < len(s) and s[l] == s[r]: 
            #     count += 1 
            #     l -= 1 
            #     r += 1 
        return count 
        