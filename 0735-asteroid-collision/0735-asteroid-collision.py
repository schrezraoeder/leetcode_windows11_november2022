class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] 
        for a in asteroids: 
            if not stack or a > 0:
                stack.append(a) # [1] 
            elif stack and stack[-1] > 0 and a < 0: # only combination for collision 
                while stack and stack[-1] > 0 and stack[-1] < abs(a):
                    stack.pop() 
                if stack and stack[-1] > 0 and abs(a) == stack[-1]: 
                    stack.pop()
                    continue 
                if stack and stack[-1] < 0:
                    stack.append(a)
                if not stack and a < 0:
                    stack.append(a) 
            elif stack and stack[-1] < 0:
                stack.append(a)
        return stack 
                
                    
                
        