# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(r,g):
            nonlocal ans

            if r is None:
                return 
            
            if r.left :
                if r.left.val >= g:
                    ans+=1
                    dfs(r.left,r.left.val)
                else:
                    dfs(r.left,g)
            if r.right :
                if r.right.val >= g:
                    ans+=1
                    dfs(r.right,r.right.val) 
                else:
                    dfs(r.right,g)
        dfs(root,root.val)
        return ans+1