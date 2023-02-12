class Solution:
    def longestPalindrome(self, s: str) -> str:
        # looked at hint 1: How can we reuse a previously computed palindrome to compute a larger palindrome?
        # then looked at hints 2 & 3. 
        # then looked at the neetcode video solution one time (still didn't feel ready to code it up after 
        # watching through the conceptual description of the algorithm) 
        longest = -1 
        answer = ''
        for i in range(len(s)): 
            l, r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                current_length = r - l + 1 
                if current_length > longest:
                    longest = current_length 
                    answer = s[l:r+1] 
                l -= 1 
                r += 1 
            l, r = i, i + 1 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                current_length = r - l + 1 
                if current_length > longest:
                    longest = current_length 
                    answer = s[l:r+1] 
                l -= 1 
                r += 1 
        return answer 
        