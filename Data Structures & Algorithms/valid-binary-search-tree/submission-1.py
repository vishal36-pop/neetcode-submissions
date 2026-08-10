# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(node,l,g):
            if node is None:
                return True
            if node.val <= l or node.val >= g :
                return False
            a = rec(node.left,l,node.val) 
            b = rec(node.right,node.val,g)
            return a and b
        return rec(root,float('-inf'),float('inf'))