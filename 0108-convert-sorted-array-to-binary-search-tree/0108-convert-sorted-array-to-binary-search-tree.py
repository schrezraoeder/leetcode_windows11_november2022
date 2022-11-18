# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def _helper(self, array):
        if not array:
            return None 
        p = len(array)//2 
        print()
        print ('p:')
        print (p) 
        print ('array:')
        print (array)
        print ('array[:p]')
        print ('array[p+1:]')
        root = TreeNode(array[p]) 
        root.left = self._helper(array[:p]) 
        root.right = self._helper(array[p+1:])
        return root 
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
 
        return self._helper(nums) 
            
            
        