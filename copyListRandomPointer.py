class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if (head == None):
            return None

        node = head
        while (node != None):
            # STEP 1
            newnode = Node(node.val)
            newnode.next = node.next
            node.next = newnode

            node = newnode.next

        # STEP 2
        node = head
        while (node != None):
            if (node.random == None):
                node.next.random = None
            else:
                node.next.random = node.random.next

            node = node.next.next

        # STEP 3
        node = head
        result = head.next
        temp = head.next

        while (node != None):
            node.next = node.next.next

            if (temp.next == None):
                temp.next = None
            else:
                temp.next = temp.next.next

            node = node.next
            temp = temp.next

        return result