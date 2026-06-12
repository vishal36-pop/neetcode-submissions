"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        curr = head
        ans = Node(head.val)
        p = ans
        #postion map
        pos = {}
        i = 0 #counter
        dup = []
        while curr is not None:
            pos[curr] = i
            if curr.next is not None:
                p.next = Node(curr.next.val)
            else:
                p.next = None
            dup.append(p)
            i+=1
            curr = curr.next
            p = p.next  
        pos[None] = i
        dup.append(None)
        #now we have a duplicate list with random empty and position of the original nodes 
        #now if we knwo at which postion which duplicate node is tehre 
        curr = head
        p = ans
        while curr is not None:
            t_p = pos[curr.random] # the postion of the node to which random is pointing to 
            p.random = dup[t_p]
            curr = curr.next
            p = p.next
        return ans















