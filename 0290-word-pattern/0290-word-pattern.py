class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        list_pattern = [item for item in pattern] 
        list_string = s.split()
        if len(list_pattern) != len(list_string):
            return False 
        map_pattern_words = {}
        for ix, item in enumerate(list_string):
            if item in map_pattern_words: 
                if list_pattern[ix] != map_pattern_words[item]:
                    return False 
            else: 
                if list_pattern[ix] in list_pattern[:ix]:
                    return False 
                map_pattern_words[item] = list_pattern[ix] 
        return True 
                