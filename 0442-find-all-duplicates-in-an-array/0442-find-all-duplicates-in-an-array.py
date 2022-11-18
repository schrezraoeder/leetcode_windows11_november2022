from collections import Counter 

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]: 
        
        q = Counter(nums) 
        w = sorted(q.items(), key = lambda x: (-x[1], x[0])) 
        print (w)
        answer = [] 
        for key, val in w: 
            if val > 1:
                answer.append(key) 
            else:
                break 
        return answer 
        
        