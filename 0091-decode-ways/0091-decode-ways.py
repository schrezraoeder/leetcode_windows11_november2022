# NOTE: after much struggle with this one, watched the Neetcode solution before coding it up 
# And I struggled so much with this one that I also watched the Knowledge Center solution[s] 
# then tried coding it up again 
class Solution: 
    def numDecodings(self, s: str) -> int:  
        if len(s) == 0: 
            return 0 
        if s[0] == '0':
            return 0 
        if len(s) == 1: 
            return 1 
        count1 = 1 # prev prev 
        count2 = 1 # prev 
        for i in range(1, len(s)):
            count = 0 
            if s[i] in '123456789':
                count += count2 
            if (s[i-1] == '1' or s[i-1] == '2' and s[i] in '0123456'):
                count += count1 
            count1 = count2 
            count2 = count 
        return count 
        
            
        
                
        
        