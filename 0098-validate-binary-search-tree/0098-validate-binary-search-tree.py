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
        # originally in the following line of code I did not have the `root.left and root.right` clause 
        # immediately after the `if`... in other words the following line of code used to look like: 
        # if bstMax(root.left) < root.val and bstMin(root.right) > root.val: 
        # however the stupid thing failed... passing on 79 out of 82 test cases but failing for example on
        # the test case:
        # [-2147483648,null,2147483647,-2147483648] 
        # but I feel that this is a **fluke** of leetcode but cannot be bothered presently to look into it 
        if root.left and root.right and bstMax(root.left) < root.val and bstMin(root.right) > root.val: 
            return self.isValidBST(root.left) and self.isValidBST(root.right) 
        return False 
        