# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        if root is None:
            root = TreeNode(val)
            return root
        def is_leaf(node):
            return (node.left is None and node.right is None)
        while True :
            if val >  curr.val :
                if curr.right is None:
                    break
                curr = curr.right
            else :
                if curr.left is None:
                    break
                curr = curr.left
        if val>curr.val :
            curr.right = TreeNode(val)
        else:
            curr.left = TreeNode(val)
        return root
        