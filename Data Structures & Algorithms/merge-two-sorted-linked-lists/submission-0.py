# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        if p1 is None:
            return p2
        if p2 is None:
            return p1

        head = None
        curr = head
        while p1 is not None and p2 is not None:
            print(p1.val,p2.val)
            if p1.val <= p2.val:
                if head is None:
                    head = p1
                    p1 = p1.next
                    curr = head
                else:
                    curr.next = p1
                    p1 = p1.next
                    curr = curr.next
            else:
                if head is None :
                    head = p2
                    p2 = p2.next
                    curr = head
                else:
                    curr.next = p2
                    p2 = p2.next
                    curr = curr.next
        if p1 is not None:
            curr.next = p1
        else:
            curr.next = p2
        return head




