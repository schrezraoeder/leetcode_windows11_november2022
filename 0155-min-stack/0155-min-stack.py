# Note: watched the neetcode solution yesterday after spending some time 
# on it & realizing O(1) for both pop & push is a *bit* tricky while maintaining a min 
class MinStack:

    def __init__(self):
        self.stack = [] 
        self.min_stack = [] 
        

    def push(self, val: int) -> None: 
        if self.stack: 
            self.stack.append(val) 
            self.min_stack.append(min(val, self.min_stack[-1])) 
        else: 
            self.stack.append(val)
            self.min_stack.append(val) 
        

    def pop(self) -> None:
        self.min_stack.pop()
        self.stack.pop() 
        

    def top(self) -> int:
        return self.stack[-1] 
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()