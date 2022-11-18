# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque 

class Solution:
    def recursive_inorder_traversal(self, o, c, target):
        if o.left:
            self.recursive_inorder_traversal(o.left, c.left, target)
        if o.val == target.val:
            self.node = c 
        if o.right:
            self.recursive_inorder_traversal(o.right, c.right, target) 
        
        
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.recursive_inorder_traversal(original, cloned, target)
        return self.node 
        
            
        
        