# NOTE: re-watched the qualitative part of a solution on youtube up to
# https://youtu.be/mJWQjJpEMa4?t=647 
# again before coding it up today 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums2 = [1, 3, 4, 2] 
        stack = [nums2[-1]] # [2] 
        greaters = [-1] # [-1] 
        for i in range(len(nums2)-2, -1, -1): 
            while stack and nums2[i] > stack[-1]: 
                stack.pop() 
                continue 
            if stack and nums2[i] < stack[-1]: 
                greaters.append(stack[-1]) 
                stack.append(nums2[i]) 
            if not stack: 
                stack.append(nums2[i]) # [-1] 
                greaters.append(-1)  # [2] 
        answer = [] 
        for num in nums1:
            ix = nums2.index(num) 
            answer.append(greaters[-ix-1]) 
        return answer 
                
                                  
                
        