import string 

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        #alphabet = string.ascii_lowercase  
        s = s.lower() 
        q = '' 
        for char in s: 
            #if char in alphabet: 
                # q += char 
                # q.isalnum()  
            if char.isalnum(): 
                q += char 
        i = 0 
        while (i < len(q)) and (q[i] == q[-i-1]): 
            i += 1 
        if i == len(q):
            return True 
        return False 
        