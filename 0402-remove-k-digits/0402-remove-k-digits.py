# trying to code it up again from memory after a little time 
# passes... originally i watched the neetcode solution
# and coded it up very shortly afterwards on the python3 tab 
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = [] 
        for char in num:
            while stack and k > 0 and stack[-1] > char: 
                stack.pop()
                k -= 1 
            if stack or char != '0':
                stack.append(char) 
        stack = ''.join(stack) 
        stack = stack[:len(stack)-k]
        if not stack: stack = '0' 
        return stack 
        
        