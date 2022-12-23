class Solution:
    def lengthOfLongestSubstring(self, a_string: str) -> int:
        if len(a_string) == 0:
            return 0 
        if len(a_string) == 1: 
            return 1
        # a_string is at least two characters 
        i = 0 
        j = 1 
        current_set = set() 
        current_set.add(a_string[i]) 
        longest = 1 
        #while the next char in a_string is not in current_set add it 
        while (i <= len(a_string) - 1) and (j <= len(a_string) - 1): 
            while (j <= len(a_string)-1) and (a_string[j] not in current_set): 
                current_set.add(a_string[j])
                j += 1 
            # 'abc' 'a' 
            # 'abca' 
            # ^   ^ 
            if len(current_set) > longest: 
                longest = len(current_set) 
            while (i <= len(a_string) - 1) and (j <= len(a_string) - 1) and a_string[i] != a_string[j]: 
                i += 1 
            i += 1 
            # 'bca'
            current_set = set(a_string[i:j+1])
            j += 1 
        return longest 
        