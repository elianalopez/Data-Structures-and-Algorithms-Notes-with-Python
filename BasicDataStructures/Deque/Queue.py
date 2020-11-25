#Queue ADT implementation in Python via a custom Queue Class.

class Queue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == [] 
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        #created an if and an elif statement to stop the errors of 
        #popping less than 0
        if len(self.items) > 0:
            return(self.items.pop())
        elif len(self.items) == 0:
            return None
    
    #added defgetFront if the length is greater than one then the front would come out
    #if it is less then none the front will return None
    def getFront(self):
        if len(self.items) > 0:
            return self.items[len(self.items)-1]
        elif len(self.items) == 0:
            return None
        
    #This is my string function! If amount of items in the list are greater than 0 then
    #the item will be stringified if it is == to 0 then it will return an empty list.
    def __str__(self):
        if len(self.items) > 0:
            return str(self.items)
        elif len(self.items) == 0:
            return str([])
