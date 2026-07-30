# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find total length
        # go to node of Before: (length - n - 1) counting from 0
        dummy = ListNode()
        dummy.next = head
        length = 0
        count = head
        while count:
            length += 1
            count = count.next
        
        before = dummy
        for _ in range(length-n): # goes from 0 to length-n-1
            before = before.next
        if before.next:
            before.next = before.next.next

        return dummy.next
