# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        rep1 = []
        rep2 = []
        def dfs(node,rep):
            if node is None :
                rep.append(None)
                return 
            rep.append(node)
            dfs(node.right,rep)
            dfs(node.left,rep)

        dfs(p,rep1)
        dfs(q,rep2)
        rep1 = list(map(lambda x: x.val if x is not None else 'None',rep1))
        rep2 = list(map(lambda x: x.val if x is not None else 'None',rep2))
        return rep1 == rep2

                
