class Solution:
    def vanilla_binary_search(self, nums, l, r, target): # returns False if not found or index of array if found
        if l == r:
            if nums[l] == target:
                return l 
            return False
        if l > r:
            return False 
        mid = l + (r - l)//2 
        if nums[mid] == target: 
            return mid 
        left_search = self.vanilla_binary_search(nums, l, mid-1, target) 
        right_search = self.vanilla_binary_search(nums, mid+1, r, target) 
        if left_search or right_search: 
            if left_search:
                return left_search
            else:
                return right_search # return's index of array if found 
        else:
            return False 
        
        
        
    def search(self, nums: List[int], target: int) -> int:
# thinking...          
#         target == k ... some value 
        
#         if there's no pivot, then the array is sorted in ascending order 
#         in that case just a normal binary search with no changes will find
#         it in log[n] time. 
        
#         if there is a pivot, either `k` is in the second "half" (after the pivot)
#         or the first "half" (before the pivot). 
        
#         [12 17 41 2 3 5 8] search 5 
#         mid == 2 
#         2 < 5 so binary search [3 .. 8] 
        
#         search 17
#         mid == 2 so do we perform two binary searches? 
        
#         you could always just do two binary searches 2*log(n) is still log(n) 
        if nums[0] == target:
            return 0 
        
        found = self.vanilla_binary_search(nums, 0, len(nums)-1, target) 
        if not found:
            return -1 
        return found 
            
        
        
        