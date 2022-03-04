class Solution:
    def oddEvenList(self, head):
        if (head == None):
            return None
        dum1 = ListNode()
        dum2 = ListNode()
        odd = dum1
        even = dum2

        count = 1
        while (head != None):
            if (count % 2 == 0):
                even.next = head
                even = head
            else:
                odd.next = head
                odd = head
            head = head.next
            count += 1

        even.next = None
        odd.next = dum2.next

        return dum1.next
