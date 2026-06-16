# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        ans = []
        while queue:
            oldfront = []
            newfront = []
            for a in queue:
                if a !=None:
                    oldfront.append(a.val)
                    if a.left!=None:
                        newfront.append(a.left)
                    if a.right!=None:
                        newfront.append(a.right)
            ans.append(oldfront)
            queue = newfront
        return ans