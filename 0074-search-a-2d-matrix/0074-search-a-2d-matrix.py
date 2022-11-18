class Solution:
    
    # return the row index where target can be found or -1 if it is outside the bounds of the matrix 
    def _which_row_game(self, matrix, target): 
        ix = -1 
        if target < matrix[0][0]:
            return ix
        for ix in range(len(matrix)):
            if matrix[ix][0] <= target and matrix[ix][(len(matrix[ix])-1)] >= target:
                return ix 
        ix = -1 
        return ix 
        
    def _binary_search_row(self, row, target): 
        # row = matrix[row_ix] 
        l = 0
        r = len(row) - 1 
        while l <= r: 
            if row[l] == target: 
                return True 
            if row[r] == target: 
                return True 
            median = l + (l + r)//2 
            if row[median] == target:
                return True
            else: 
                return self._binary_search_row(row[l:median], target) or self._binary_search_row(row[median+1:], target) 
        
        
        
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # IDEA: do a binary search on the rows, first. 
        # just use the first entry in each row as a proxy to which row the target will be found in 
        row_ix = self._which_row_game(matrix, target) 
        if row_ix == -1:
            return False 
        row = matrix[row_ix] 
        return self._binary_search_row(row, target) 
        
        