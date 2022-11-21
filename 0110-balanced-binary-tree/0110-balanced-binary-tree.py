# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from math import abs 

class Solution(object):
    def height(self, node):
        if not node:
            return 0 
        if not node.left:
            return 1 + self.height(node.right)
        if not node.right:
            return 1 + self.height(node.left) 
        return 1 + max(self.height(node.left), self.height(node.right)) 
    
    def leftHeight(self, node):
        if not node:
            return 0 
        if not node.left:
            return 1
        return 1 + self.height(node.left) 
    
    def rightHeight(self, node):
        if not node:
            return 0 
        if not node.right:
            return 1
        return 1 + self.height(node.right)
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: 
            return True 
        if not root.left:
            return self.height(root.right)  <= 1 
        if not root.right:
            return self.height(root.left) <= 1 
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right) 
        