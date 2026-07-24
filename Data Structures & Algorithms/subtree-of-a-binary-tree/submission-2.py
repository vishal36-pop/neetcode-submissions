# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a,b):
            # print(a is None ,b is None)
            if a is None and b is None:
                return True
            elif (a is None) ^ (b is None):
                return False
            if a.val != b.val:
                return False
            ans = True
            ans = ans and same(a.left,b.left) 
            ans = ans and same(a.right,b.right)
            return ans
        def issub(a):
            if a is None:
                return False
            if same(a,subRoot):
                return True
            else:
                ans = (issub(a.left) ) or (issub(a.right) )
            return ans
        return issub(root)

