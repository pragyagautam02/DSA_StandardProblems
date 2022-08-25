class Stack:
    def __init__(self,size):
        self.stack = []
        self.size = size

    def isFull(self):
        return len(self.stack) == self.size
        
    def isEmpty(self):
        return len(self.stack) == 0
        
    def push(self,ele):
        if self.isFull():
            return "Stack is Full"

        else:
            self.stack.append(ele)
            
    def pop(self):
        if self.isEmpty():
            return -1

        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]

s = Stack(10)
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.pop())
s.push(40)
print("Peek : ",s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print("Peek : ",s.peek())
