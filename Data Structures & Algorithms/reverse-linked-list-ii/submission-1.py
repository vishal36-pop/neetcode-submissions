# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        curr = head
        prev = None
        #start reversing when the i == l+1
        #assign the prev when i == l
        #assign the lbl when i = l-1
        lth = None
        lb1 = None
        if left == 1:
            lb1 = None
        while i <= right and curr is not None:
            if i < left-1 :

                i+=1
                curr = curr.next
                continue
            if i == left-1:

                lb1 = curr
                curr = curr.next
                i+=1
                continue
            if i == left:
                prev = curr
                lth = curr
                curr = curr.next
                i+=1
                continue
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i+=1
        print(prev.val)
        if lb1 is not None:
            lb1.next = prev
        else:
            head = prev
        lth.next = curr
        return head






            