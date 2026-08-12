# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inndx,prendx = 0,0
        def rec(limit):
            nonlocal inndx,prendx
            if prendx >=len(preorder):
                return None
            if inorder[inndx] == limit:
                inndx += 1 
                return None
            
            root = TreeNode(preorder[prendx])
            prendx +=1
            root.left = rec(root.val)
            root.right = rec(limit)
            return root
        return rec(float('inf'))