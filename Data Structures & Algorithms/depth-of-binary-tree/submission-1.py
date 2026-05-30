# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #depth of the tree is defined as the no of edges from the root to currnode
        if root is None :
            return 0
        ans = 0
        d_array = dict()
        d_array[root] = 0
        def depth(node):
            nonlocal ans
            if node is None :
                return
            if node.left is not None:
                d_array[node.left] = d_array[node]+1
                depth(node.left)
                ans = max(ans,d_array[node.left])
            if node.right is not None:
                d_array[node.right] = d_array[node]+1
                depth(node.right)
                ans = max(ans,d_array[node.right])
            return 
        depth(root)
        return ans+1
                

