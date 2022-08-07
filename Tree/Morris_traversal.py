class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertion(self,root,key):
        if not root:
            return TreeNode(key)

        elif(key <= root.val):
            root.left = self.insertion(root.left,key)

        else:
            root.right = self.insertion(root.right,key)

        return root

    def Morris_traversal(self,root):
        self.inorder = []
        
        while(root):
            if not root.left:
                self.inorder.append(root.val)
                root = root.right
            else:
                left_subtree = root.left
                while(left_subtree.right and left_subtree.right != root):
                    left_subtree = left_subtree.right

                #When (left_subtree.right) condition fails
                if(not left_subtree.right):
                    left_subtree.right = root
                    root = root.left

                #When (left_subtree.right != root) condition fails
                else:
                    left_subtree.right = None
                    self.inorder.append(root.val)
                    root = root.right

        return self.inorder


                

    #Normal Inorder Traversal using Recursion
    def inorder(self,root):
        if not root:
            return

        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    

r = TreeNode(50)
s = Solution()
r = s.insertion(r,30)
r = s.insertion(r,20)
r = s.insertion(r,40)
r = s.insertion(r,70)
r = s.insertion(r,60)
r = s.insertion(r,80)

#s.inorder(r)
print(s.Morris_traversal(r))

    
