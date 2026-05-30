# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            #no nodes in the paths so return 
            return 0 
        #maxdepth == maxheight of the tree
        #max height is defined as the max(no of edges from the leafnodes to node) #from leaf to node is height
        def height(node):
            if node is None:
                return 0 #this assumes the leafs height as 1 since is both left and right are nones then the height of the leaf is 1
            return max(height(node.left),height(node.right))+1
        return height(root)