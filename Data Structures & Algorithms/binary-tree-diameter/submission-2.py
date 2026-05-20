# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        from collections import defaultdict

        def isleaf(node):
            if node.left is None and node.right is None :
                return True
            else:
                return False
        
        parent = {root: None}
        depth = {root : 0 }
        height = defaultdict(int)
        def dfs(node):
            if isleaf(node):
                height[node] = 0 
                return 0
            if node.left is not None:
                parent[node.left] = node
                depth[node.left] = depth[node]+1
                height[node] = dfs(node.left)+1
            if node.right is not None:
                parent[node.right] = node
                depth[node.right] = depth[node]+1
                height[node] = max(height[node],dfs(node.right)+1)
            return height[node]
        height[root] = dfs(root)
        oneend = max(depth,key = depth.get)

        ans = -1 # this is used to see the height of the parent nodes otherside
        if oneend == root:
            return 0
        while True :
            p = parent[oneend]
            if p is None :
                break
            if p.left == oneend:
                if p.right is not None:
                    if ans < height[p.right]+1+height[p]:
                        ans = height[p.right]+1+height[p]
                else:
                    if ans < height[p]:
                        ans = height[p]
            if p.right == oneend:
                if p.left is not None :
                    if ans < height[p.left]+1+height[p]:
                        ans = height[p.left]+1+height[p]
                else:
                    if ans < height[p]:
                        ans = height[p]

            oneend = p    
        return ans
            

        