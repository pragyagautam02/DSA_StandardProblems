class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.temp=None

    def insert_begin(self,data):
        if self.head is None:
            self.head=Node(data)
            self.head.next=None
        else:
            self.new_node=Node(data)
            self.new_node.next=self.head
            self.head=self.new_node
            
    def insert_end(self,data):
        if self.head is None:
            self.head=Node(data)
            self.head.next=None
        else:
            self.new_node=Node(data)
            self.temp=self.head
            while(self.temp.next != None):
                self.temp=self.temp.next
            self.temp.next=self.new_node
            self.new_node=None
            
    def insert_pos(self,data,pos):
        if self.head is None:
            self.head=Node(data)
            self.head.next=None
        else:
            self.new_node=Node(data)

            self.temp=self.head
            while(self.temp.data != pos):
                self.temp=self.temp.next

            self.new_node.next=self.temp.next
            self.temp.next=self.new_node
    
    def display(self):
        if self.head is None:
            print("Underflow!!")
        else:
            self.temp=self.head
            while(self.temp != None):
                print(str(self.temp.data)+" -> ",end=" ")
                self.temp=self.temp.next
            print("None")
                
l1=LinkedList()
print("For Insertion at Begin ")
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.display()
print("\nFor Insertion at End ")
l1.insert_end(int(input("enter element : ")))
l1.insert_end(int(input("enter element : ")))
l1.insert_end(int(input("enter element : ")))
l1.display()
print("\nFor Insertion at Specified Position ")
l1.insert_pos(int(input("enter element : ")),int(input("enter position : ")))
l1.insert_pos(int(input("enter element : ")),int(input("enter position : ")))
l1.display()
