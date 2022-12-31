# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bstMax(node):
            while node.right:
                node = node.right 
            return node.val 
            
        def bstMin(node): 
            while node.left:
                node = node.left 
            return node.val 
        
        if not root:
            return True 
        if root.left:
            if root.left.val >= root.val:
                return False 
        if root.right:
            if root.right.val <= root.val:
                return False 
        if not root.left and not root.right: 
            return True 
        if not root.left: 
            if bstMin(root.right) > root.val:
                return self.isValidBST(root.right) 
        if not root.right:
            if  bstMax(root.left) < root.val:
                return self.isValidBST(root.left)   
        if root.left and root.right and bstMax(root.left) < root.val and bstMin(root.right) > root.val: 
            return self.isValidBST(root.left) and self.isValidBST(root.right) 
        return False 
        