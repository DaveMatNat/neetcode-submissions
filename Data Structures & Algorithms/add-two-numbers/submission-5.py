# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1 = l1
        d2 = l2
        curr = dummy = ListNode()
        carry = 0
        while d1 or d2 or carry:
            num1 = d1.val if d1 else 0
            num2 = d2.val if d2 else 0
            s = num1+num2+carry
            carry = s // 10
            digit = s % 10
            curr.next = ListNode(digit)
            curr = curr.next
            d1 = d1.next if d1 else None
            d2 = d2.next if d2 else None
        if carry != 0:
            curr.next = ListNode(carry)

        return dummy.next