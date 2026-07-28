# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr, nex = None, head, head
        while curr:
            nex = nex.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev