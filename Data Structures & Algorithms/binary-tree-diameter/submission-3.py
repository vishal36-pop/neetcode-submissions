# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #much simpler version
        #d = heightleft+heightright+2 '''+2 because 2 edges it at max  so if left or right  is none +1
        self.max = 0
        def height(node):
            global maxd
            if node is None:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            diam = lh+rh #diameter of the current node
            self.max = max(diam,self.max)
            return 1+max(lh,rh)
        height(root)
        return self.max
