class Solution: 
    def isHappy(self, n: int) -> bool:
        def helper(n, dp):
            if n == 1:
                return True 
            n = str(n) 
            new_n = 0 
            for digit in n: 
                new_n += int(digit)**2 
            n = new_n 
            if n in dp: 
                return False 
            dp.add(n)  
            return helper(n, dp) 
        return helper(n, set()) 
    
         
        
        
        