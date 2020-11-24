#Stack ADT implementation in Python via a custom Stack Class.
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.item.append(item) #adds an item to the stack

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop() #removes and returns item
        elif len(self.items) == 0:
            return None

    def peek(self):
        #make an if-else on how to return it
        if len(self.items) > 0:
            return self.items[-1]
            #returns to the top of the stack, but does not remove it
            #return(self.items[len(self.items)-1]) an alternative
        elif len(self.items) == 0:
            return None

    def isEmpty(self):
        return self.items == []
        #an alternative: return self.size() == 0

    def size(self):
        return len(self.items)
 
    #for i in a list would print each item in the list. 
    def __str__(self):
        s = "["
        for i in self.items:
            s +=  str(i)
            #this would create a space for each item printed within the list
            if self.items.index(i) !=(len(self.items)-1):
                s += ", "  
        s +=   "]" 
        return s
