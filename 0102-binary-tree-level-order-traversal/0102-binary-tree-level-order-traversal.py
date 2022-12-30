# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # heavily influenced by: 
        # https://youtu.be/6ZnyEApgFYg?t=553 
        # as i had struggled on my own with this one for a certain amount of time first 
        levels = [] 
        queue = deque()
        queue.append(root) 
        while queue: 
            max_level_length = len(queue) 
            current_level = [] 
            for i in range(max_level_length): 
                next_node = queue.popleft() 
                if next_node: 
                    current_level.append(next_node.val)
                    queue.append(next_node.left) # could be null 
                    queue.append(next_node.right) # could be `None` as well 
            if current_level: # could have had only None's at this level in the queue 
                levels.append(current_level)
        return levels 
                    

        