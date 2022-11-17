# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _flatten(self, a_list):
        answer = [] 
        for item in a_list:
            if type(item) is list:
                item = self._flatten(item)
            if type(item) is list:
                for element in item:
                    answer.append(element) 
            else: 
                answer.append(item) 
        return answer 
            
                
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = [] 
        if root:
            if root.left:
                prefix = self.inorderTraversal(root.left)
                answer = prefix 
            answer.append(root.val)
            if root.right:
                postfix = self.inorderTraversal(root.right)
                answer.append(postfix) 
        answer = self._flatten(answer) 
        return answer 
        