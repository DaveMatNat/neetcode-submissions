# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2: # while both are not empty
            if list1.val < list2.val: # if l1's val < l2's
                tail.next = list1 # set the back of the linkedlist to this value l1
                list1 = list1.next # l1 pointer moves to the next
            else: # if l2's val <= l1's 
                tail.next = list2 # set the back of the linkedlist to this value l2
                list2 = list2.next # l2 pointer moves to the next
            tail = tail.next # set the tail to the end of the linkedlist (the recently added node)

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next