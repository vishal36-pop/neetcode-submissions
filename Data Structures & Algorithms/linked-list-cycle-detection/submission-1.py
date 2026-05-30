# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashset = set()
        curr = head 
        while curr is not None:
            if curr in hashset:
                return True 
            hashset.add(curr)
            curr = curr.next
        return False