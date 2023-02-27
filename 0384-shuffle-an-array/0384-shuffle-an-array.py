from random import randrange 
class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums[:] # make a copy for reset purposes 
        

    def reset(self) -> List[int]:
        return self.array 
        

    def shuffle(self) -> List[int]:
        shuffled_array = self.array[:] 
        for i in range(len(self.array)):
            swap_ix = randrange(len(self.array)) 
            shuffled_array[i], shuffled_array[swap_ix] = shuffled_array[swap_ix], shuffled_array[i]
        return shuffled_array 
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()