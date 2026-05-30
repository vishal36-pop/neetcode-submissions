# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        d = -1 # d keeps track of the max no of nodes in the longest path between two vertices 
        def height(node):
            nonlocal d 
            if node is None:
                return 0
            hleft = height(node.left)
            hright = height(node.right)
            d = max(d,hleft+hright+1)
            return max(hleft,hright)+1
        height(root)
        return d-1 #since the no of edges = no of nodes -1 
            
        