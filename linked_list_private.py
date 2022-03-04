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
        
    def insert_end(self,data):
        new_node=Node()
        new_node.set_data(data)
        if self.get_head()==None:
            self.__head=self.__tail=new_node
        else:
            self.__tail.set_next(new_node)
            self.__tail=new_node
            
    def insert_pos(self,data,pos):
        new_node=Node()
        new_node.set_data(data)
        if self.get_head()==None:
            self.__head=self.__tail=new_node
        else:
            temp=self.__head
            while(temp.get_data() != pos):
                temp=temp.get_next()
            new_node.set_next(temp.get_next())
            #new_node.next=self.temp.get_next()
            temp.set_next(new_node)
            
    def del_begin(self):
        if self.get_head()== None:
            print("Underflow!!")
        else:
            self.__head=self.__head.get_next()

    def del_end(self):
        temp=self.__head
        if self.get_head()== None:
            print("Underflow!!")
        else:
            while(temp.get_next()!= self.__tail):
                    temp=temp.get_next()
            self.__tail=temp
            

    def del_pos(self,pos):
        if self.get_head()==None:
            print("Underflow!!")
        else:
            temp=self.__head
            if(pos==self.__head.get_data()):
                self.__head=self.__head.get_next()
            elif(pos==self.__tail.get_data()):
                while(temp.get_next()!= self.__tail):
                    temp=temp.get_next()
                self.__tail=temp
                
            else:
                temp=self.__head
                while(temp.get_next().get_data() != pos):
                    temp=temp.get_next()
                
                temp.set_next(temp.get_next().get_next())

    def display(self):
        self.temp=self.__head
        while(self.temp != self.__tail):
            print(str(self.temp.get_data())+" -> ",end=" ")
            self.temp=self.temp.get_next()
        print(str(self.temp.get_data())+" -> None",end=" ")

l1=LinkedList()
print("\nFor Insertion at End ")
l1.insert_end(int(input("enter element : ")))
l1.insert_end(int(input("enter element : ")))
l1.insert_end(int(input("enter element : ")))
l1.insert_end(int(input("enter element : ")))
l1.insert_end(int(input("enter element : ")))
l1.display()
print("For Insertion at Begin ")
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.insert_begin(int(input("enter element : ")))
l1.display()
print("\nFor Insertion at Specified Position ")
l1.insert_pos(int(input("enter element : ")),int(input("enter position : ")))
l1.insert_pos(int(input("enter element : ")),int(input("enter position : ")))
l1.display()
print("\nFor Deletion from Pos ")
l1.del_pos(int(input("enter element : ")))
l1.display()
print("\nFor Deletion from Begin ")
l1.del_begin()
l1.display()
print("\nFor Deletion from End ")
l1.del_end()
l1.display()
        

        
