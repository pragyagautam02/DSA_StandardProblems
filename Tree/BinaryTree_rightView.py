from collections import deque

class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root,ans):
    if not root:
        return

    inorder(root.left,ans)
    ans.append(root.val)
    inorder(root.right,ans)
        


class Solution:
    
    def rightView(self,root):
        self.right_view = []
        def bfs(root):
            queue = deque()
            queue.append(root)

            while(queue):
                l = len(queue)
                #self.right_view.append(queue[-1].val)
                for i in range(l):
                    curr = queue.popleft()

                    if curr.left:
                        queue.append(curr.left)

                    if curr.right:
                        queue.append(curr.right)
                        
                
                self.right_view.append(curr.val)
            return self.right_view

        return bfs(root)
                


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.right.right = Node(4)

#ans = []
#inorder(root,ans)
#print(ans)

s = Solution()
print(s.rightView(root))
