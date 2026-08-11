# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ans = None
        def rec(node):
            nonlocal cnt
            nonlocal ans
            if node is None or ans is not None:
                return 
            rec(node.left)
            cnt+=1
            if cnt == k:
                ans = node.val
                return 
            rec(node.right)
            #do an inorder traversal 
        rec(root)
        return ans