# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = None 
        curr = root
        found = True
        while curr.val != key :
            if key> curr.val :
                if curr.right is None:
                    found = False
                    break
                parent = curr
                curr = curr.right
            if key < curr.val :
                if curr.left is None:
                    found = False
                    break
                parent = curr
                curr = curr.left
        if found is False:
            return root
        
        #now we have found the node
        #if node is root:
        #simply replace the root with root.right if root.rihgt is not none
        if parent is None:
            if curr.right is not None:
                root = curr.right
            else:
                root = curr.left
                return root
        
        #if node is not root
        #replace the parent.right if curr is right else replace p.left with curr.right (if curr.right is not none)

        #case 1 curr.right is none:
        if parent is not None and curr.right is None:
            if parent.left is curr:
                parent.left = curr.left
            else:
                parent.right = curr.left
            return root
        
       #case2 if curr.right is not none 
        if parent is not None:
            if parent.left is curr:
                parent.left = curr.right
            else:
                parent.right = curr.right
        
        #now find a place for the curr.left for insertion 
        if curr.left is None:
            return root
        val = curr.val 
        spot= root
        while True:
            if val<spot.val:
                if spot.left is None:
                    break
                spot = spot.left
            if val>spot.val:
                if spot.right is None:
                    break
                spot = spot.right
        if val < spot.val:
            spot.left = curr.left
        else:
            spot.right = curr.left
        return root
            
        
        

                    

                
