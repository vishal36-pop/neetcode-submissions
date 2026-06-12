# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        prev = None
        while curr is not None:
            size+=1
            prev = curr
            curr = curr.next
        if size == 1:
            return None
        #we want the size-n to be deleted (o indexed)
        target = size-n
        i = 0
        curr = head
        prev = None
        while i < size-n:
            prev = curr
            curr =  curr.next
            i+=1
        if n == size:
            temp = curr.next
            curr.next = prev
            head = temp
            return head
        elif n == 1:
            prev.next = None
            return head
        else:
            temp = curr.next
            prev.next = temp
            return head


        