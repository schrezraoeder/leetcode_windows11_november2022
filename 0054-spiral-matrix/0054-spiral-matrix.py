# Note: struggled with this one for more than half an hour then watched 
# Neetcode.io solution before coding it up 
# https://youtu.be/BJnMZNwUk1M 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]: 
        left = 0 
        right = len(matrix[0]) 
        top = 0 
        bottom = len(matrix) 
        solution = [] 
        while left < right and top < bottom: 
            for i in range(left, right): 
                solution.append(matrix[top][i]) 
            top += 1 
            for i in range(top, bottom):
                solution.append(matrix[i][right-1]) 
            right -= 1 
            if left >= right or top >= bottom:
                break
            for i in range(right - 1, left - 1, -1):
                solution.append(matrix[bottom-1][i])
            bottom -= 1 
            for i in range(bottom - 1, top - 1, -1):
                solution.append(matrix[i][left]) 
            left += 1 
        return solution 
                
        