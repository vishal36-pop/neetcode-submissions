# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        p3 = None
        prev = None
        carry = 0
        while p1 or p2 or carry:
            a = p1.val if p1 else 0
            b = p2.val if p2 else 0
            c = a+b+carry
            carry = c//10
            digit = c%10
            print(carry,digit)
            if p3 is None:
                p3 = ListNode(digit)
                prev = p3
                p1 = p1.next if p1 else None
                p2 = p2.next if p2 else None
                continue
            prev.next = ListNode(digit)
            prev = prev.next
            p2 = p2.next if p2 else None
            p1 = p1.next if p1 else None
        return p3