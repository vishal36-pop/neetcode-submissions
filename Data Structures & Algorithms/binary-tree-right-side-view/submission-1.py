# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #we will just do level bfs on the tree select the last one in level
        if root is None:
            return []
        q = [root]
        visited = set()
        ans = []
        while q :
            #q consists of the current level so add the last element in the ans
            ans.append(q[-1].val)
            next_level = []
            for u in q:
                if u.left is not None:
                    next_level.append(u.left)
                if u.right is not None:
                    next_level.append(u.right)
            q = next_level
        return ans