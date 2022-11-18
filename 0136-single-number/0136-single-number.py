class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = dict() 
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1 
            else:
                hash_table[num] = 1 
        for key, value in hash_table.items():
            print (key)
            print (value)
            print ()
            if value == 1:
                return key 
            
        