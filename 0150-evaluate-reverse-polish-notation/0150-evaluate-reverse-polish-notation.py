from operator import mul, add, sub, truediv 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # push non-operators; if we see an operator, pop the last two  
        op = {'+': add, '-': sub, '*': mul, '/': truediv}
        for token in tokens: 
            # if token in '+-/*':
                # b, a = stack.pop(), stack.pop()
                # result = int(op[token](a, b)) # round *toward* zero  
                # stack.append(result)  
                
            stack.append(int(op[token](stack.pop(-2), stack.pop())) if token in '+-/*' else int(token)) 
            # else: 
            #     stack.append(int(token)) 
        return stack[-1]
                
        