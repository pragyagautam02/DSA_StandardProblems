# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        midN = self.midList(head)
        second = self.reverseMidList(midN)
        first = head

        while (second.next != None):
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp

    def midList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseMidList(self, second: Optional[ListNode]) -> Optional[ListNode]:
        curr = second
        prev = None
        next = None

        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev