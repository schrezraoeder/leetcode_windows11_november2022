class Solution:
    # self.make_key('eat') 
    # 'lexicographically' or alphabetically order the letters into an "anagram" word 
    def make_key(self, a_string): 
        # magic 
        # black box 
        key = ''.join(sorted(a_string)) # ''.join(['a', 'e', 't']) ==> 'aet' # O(M*log[M]) 

        return key 



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {} 
        for key in strs: # O(N) N == # of str's 
            llave = self.make_key(key) # 'eat', 'ate', 'tea' 
            if llave in hash_map: 
                hash_map[llave].append(key) 
            else: 
                hash_map[llave] = [key] # 'eat'   {<llave>: ['eat']} 
        return list(hash_map.values())
        