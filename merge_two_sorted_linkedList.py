class Node:
    def __init__(self,data=None):
        self.__data=data
        self.__next=None
    def get_data(self):
        return self.__data
    def set_data(self,data):
        self.__data=data
    def get_next(self):
        return self.__next
    def set_next(self,new_node):
        self.__next=new_node
        
        
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    def get_head(self):
        return self.__head
    def set_head(self,new_node):
        self.__head=new_node
    def get_tail(self):
        return self.__tail
    def set_tail(self,tail):
        self.__tail=tail

    def insert_begin(self,data):
        if self.get_head()== None:
            self.__head=Node(data)
            self.__head.set_next(None)
        else:
            self.new_node=Node(data)
            self.new_node.set_next(self.__head)
            self.__head=self.new_node

    def display(self):
        self.temp=self.__head
        while(self.temp != self.__tail):
            print(str(self.temp.get_data())+" -> ",end=" ")
            self.temp=self.temp.get_next()
        #print(self.temp.get_data(),end=" ")

def merge(temp1,temp2):
    temp1=temp1.get_head()
    temp2=temp2.get_head()
    
    merge_list=LinkedList()
    head_ptr=merge_list.get_head()

    while temp1 or temp2:
        new_node=Node()
        if(temp1.get_data() <= temp2.get_data()):
            new_node.set_data(temp1.get_data())
            temp1=temp1.get_next()
        else:
            new_node.set_data(temp2.get_data())
            temp2=temp2.get_next()
        merge_list.insert_begin(new_node)

    while(temp1):
        new_node.set_data(temp1.get_data())
        merge_list.insert_begin(new_node)
        temp1=temp1.get_next()
    while(temp2):
        new_node.set_data(temp2.get_data())
        merge_list.insert_begin(new_node)
        temp2=temp2.get_next()
        
    return head_ptr


l1=LinkedList()
print("\nFirst Sorted Linked List : ")
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.display()

l2=LinkedList()
print("\nSecond Sorted Linked List : ")
l2.insert_begin(int(input("enter element : ")))
l2.insert_begin(int(input("enter element : ")))
l2.insert_begin(int(input("enter element : ")))
l2.display()

#print(l1.get_head(),l2.get_head())

l3=LinkedList()
print("\nMerging First and Second Linked List : ")
l3.set_head(merge(l1.get_head(),l2.get_head()))
l3.display()
