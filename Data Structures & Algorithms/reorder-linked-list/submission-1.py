# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        size = 0
        curr = head
        while curr is not None:
            curr = curr.next
            size+=1
        if size <=2:
            return 
        #we now know the length of the list
        curr = head
        i = 0
        head2 = None
        prev = None #for the second half of the list 
        while curr is not None:
            if i <= (size//2) - 1:
                curr = curr.next
                i+=1
                continue
            if i == (size//2):
                temp = curr.next
                curr.next = None
                curr = temp
                i+=1
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i+=1
        head2 = prev
        #merge the two list 
        p = head
        q = head2
        while p is not None and q is not None:
            temp1 = p.next
            temp2 = q.next
            p.next = q
            q.next = temp1
            p = temp1
            q = temp2
        




        