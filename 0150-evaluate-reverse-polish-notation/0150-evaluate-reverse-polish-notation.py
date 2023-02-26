from operator import mul, add, sub, truediv 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # push non-operators; if we see an operator, pop the last two  
        op = {'+': add, '-': sub, '*': mul, '/': truediv}
        ops = '+-/*'
        for token in tokens: 
            stack.append(int(op[token](stack.pop(-2), stack.pop())) if token in ops else int(token)) 
        return stack[-1]
                
        