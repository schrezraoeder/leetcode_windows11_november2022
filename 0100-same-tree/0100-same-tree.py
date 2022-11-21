# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # if not p and not q:
        #     return True 
        # elif not p and q: 
        #     return False 
        # elif not q and p:
        #     return False 
        if not p or not q:
            return not p and not q 
        if not p.left and not p.right:
            if not q.left and not q.right:
                return p.val == q.val 
            else: 
                return False 
        if p.val == q.val: 
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
        