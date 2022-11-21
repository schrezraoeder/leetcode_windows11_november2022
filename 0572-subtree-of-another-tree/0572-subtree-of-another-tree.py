# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # from my solution to: https://leetcode.com/problems/same-tree 
    def is_same_tree(self, p, q):
        if not p or not q:
            return not p and not q 
        if not p.left and not p.right:
            if not q.left and not q.right:
                return p.val == q.val 
            else: 
                return False 
        if p.val == q.val: 
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right) 
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not root:
            return False 
        return self.is_same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        