# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}
        parent[root] = None
        queue = collections.deque([root])
        while queue :
            u = queue.popleft()
            if u.left:
                parent[u.left] = u
                queue.append(u.left)
            if u.right:
                parent[u.right] = u
                queue.append(u.right)
        #get all the ancestors of p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q :
            if q in ancestors:
                return q
            q = parent[q]
        

            


