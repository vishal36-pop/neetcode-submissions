# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        ans = True
        def height(node):
            nonlocal ans #we have to modify the ans to true or false which is an immutable data type so nonlocal is used 
            if node is None:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            cond = abs(lh-rh)<=1
            ans = (ans and cond)
            return max(lh,rh)+1
        #height(root) returns the no of nodes on the path from the root to leaves
        height(root)
        return ans 

