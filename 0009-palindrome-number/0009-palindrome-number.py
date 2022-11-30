class Solution(object):
    def palindromic_string(self, q):
        return q == ''.join(list(reversed(q))) 
    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False 
        x = str(x) 
        return self.palindromic_string(x) 
        
        