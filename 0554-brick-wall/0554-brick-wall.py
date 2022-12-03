# from a coaching session I had with a FAANG+ engineer 
# on 12.3.2022. I had not seen this problem before & was
# able to come up with a solution. I had a few hints, mostly
# in the [Socratic] form of questions. Without that I would
# most likely have wasted *space* in my code. It took me
# *longer* than it needs to for interviews. Just where I'm 
# at right now.  

# We can turn each row into a list of where the gaps are instead of the widths of the bricks. 
# And doing that is pretty easy:
  
#   for example, 
#   	brick widths:
#       [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
#     gap locations:
#       [[1,1+2,1+2+2], [3, 3+1], [1, 1+3] [2], [3, 3+1], [1, 1+3, 1+3+1]] ==> 
#       [[1,3,5],  # O(m*n^2) time complexity # O(n) space 
#        [3,4],
#        [1, 4], 
#        [2],
#        [3,4],
#        1,4,5]] 
#     Naive Brute force solution: 
#       O(n*m)
#       look at every gap (not 0 or 6==?N):
#         ask the question, how many brick walls include that gap? 
#         [1,2,3,4,5] --> 3 rows contain the 1 gap so it *hits* 3 brick walls if we put the line down at `1` --> 6-3 == 3. 
#         [2] --> 5 
#         [3] --> 3 
#         [4] --> 2* 
#         [5] --> 4 
#       # O(n*m) time complexity # O(n) space 
#       {1: <count>,
#        2: <count>,
#        3: <count of hits>, 
#        4: <count of hits>,
#        5: <count of hits>} 

class Solution:
    # # wall is a list of lists like [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]  
    def leastBricks(self, wall: List[List[int]]) -> int:
        width = 0 
        for brick_width in wall[0]: 
            width += brick_width
        gap_counts = {}  # dictionary containing the gaps between bricks for each row 
        for row in wall: 
            row_length = len(row) 
            current_gap_location = 0 
            for ix, brick_width in enumerate(row): 
                if ix == len(row) - 1:
                    break 
                current_gap_location += brick_width 
                if current_gap_location in gap_counts: 
                    gap_counts[current_gap_location] -= 1 
                else: 
                    gap_counts[current_gap_location] = len(wall) - 1 
        if not gap_counts:
            return len(wall) 
        return min(gap_counts.values()) 
        