# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        newHead = None
        newH = None
        while (l1 != None or l2 != None):

            if (l1 != None):
                carry += l1.val
                l1 = l1.next

            if (l2 != None):
                carry += l2.val
                l2 = l2.next

            if (newHead == None):
                newHead = ListNode(carry % 10)
                newH = newHead
            else:
                newH.next = ListNode(carry % 10)
                newH = newH.next
            carry = carry // 10
        if (carry != 0):
            newH.next = ListNode(carry)

        return newHead

