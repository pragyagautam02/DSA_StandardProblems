# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        
        pre = dummy
        curr = dummy
        after = dummy
        
        #counting the length of LinkedList
        count = 0
        while(curr.next):
            count += 1
            curr = curr.next
            
        while(count >= k):
            curr = pre.next
            after = curr.next
            
            for i in range(1,k):
                curr.next = after.next
                after.next = pre.next
                pre.next = after
                after = curr.next
            
            pre = curr
            count -= k
            
        return dummy.next
        
