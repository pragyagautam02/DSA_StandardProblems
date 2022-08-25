class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left =left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
        self.ans = []

    def insert(self,ele):
        def insert_alternative(ele,root):
            if ele < root.val:
                if root.left:
                    insert_alternative(ele,root.left)
                else:
                    root.left = Node(ele)

            else:
                if root.right:
                    insert_alternative(ele,root.right)
                else:
                    root.right = Node(ele)

            
        if not self.root:
            self.root = Node(ele)

        else:
            insert_alternative(ele,self.root)

    def inorder(self,root):
        if not root:
            return

        self.inorder(root.left)
        self.ans.append(root.val)
        self.inorder(root.right)

        return self.ans

t = Tree()
t.insert(3)
t.insert(4)
t.insert(0)
t.insert(8)
t.insert(2)
print(t.inorder(t.root))
