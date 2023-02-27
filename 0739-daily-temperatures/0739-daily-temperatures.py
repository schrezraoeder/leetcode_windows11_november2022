class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [len(temperatures)-1] # monotonic increasing stack
        indexes = [0] * len(temperatures)
        for ix in range(len(temperatures)-2, -1, -1): 
            while stack and temperatures[ix] >= temperatures[stack[-1]]:
                stack.pop() 
            if stack and temperatures[ix] < temperatures[stack[-1]]:
                indexes[ix] = stack[-1] - ix 
                stack.append(ix) 
            if not stack:
                stack.append(ix) 
        return indexes 
            
            