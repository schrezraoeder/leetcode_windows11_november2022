# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # This solution is basically identical to:
        # https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/All-DFS-traversals-(preorder-inorder-postorder)-in-Python-in-1-line 
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        else:
            return [] 
        
        # my solution was: 
# class Solution:
#     def _flatten(self, a_list):
#         answer = [] 
#         for item in a_list:
#             if type(item) is list:
#                 item = self._flatten(item)
#             if type(item) is list:
#                 for element in item:
#                     answer.append(element) 
#             else: 
#                 answer.append(item) 
#         return answer 
            
                
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         answer = [] 
#         if root:
#             if root.left:
#                 prefix = self.inorderTraversal(root.left)
#                 answer = prefix 
#             answer.append(root.val)
#             if root.right:
#                 postfix = self.inorderTraversal(root.right)
#                 answer.append(postfix) 
#         answer = self._flatten(answer) 
#         return answer 
        
        