#"inheriting from Queue" 
#self.item is the thing of items
#self.items is the list itself
import Queue

class Deque(Queue.Queue):
    def __init__(self):
        super().__init__()#invokes the parent method
        
    def addRear(self, item):
        super().enqueue(item)
        
    def removeFront(self):
        return super().dequeue()
    
    def addFront(self,item):
        self.items.append(item)
    
    def removeRear(self):
        return (self.items.pop(0))
    
#don't need to implement size or isEmpty because we can
#get them from queue
