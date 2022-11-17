class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]  
            
        # I like my solution from today (above) much better than my
        # solution from 3+ weeks ago on October 25th (below)
        
        # if len(s) % 2 == 1: 
        #     breakpoint = len(s)//2 
        # if len(s) % 2 == 0: 
        #     breakpoint = len(s)//2 - 1 
        # for ix, char in enumerate(s):  
        #     if ix > breakpoint:
        #         break 
        #     s[ix], s[len(s)-ix-1] = s[len(s)-ix-1], s[ix]
        