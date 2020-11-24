#Stack ADT implementation in Python via a custom Stack Class.
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.item.append(item) #adds an item to the stack

    def pop(self):
        return self.items.pop() #removes and returns item

    def peek(self):
        return self.items[-1]
        #returns to the top of the stack, but does not remove it
        #return(self.items[len(self.items)-1])

    def isEmpty(self):
        return self.items == []
        #return self.size() == 0

    def size(self):
        return len(self.items)
        
