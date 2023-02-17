class Solution:
    memo = {} 
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        if n in self.memo:
            return self.memo[n] 
        self.memo[n] = self.fib(n-1) + self.fib(n-2) 
        return self.memo[n] 
        