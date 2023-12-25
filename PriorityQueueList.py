class PriorityQueueList:

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not bool(self.items)
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        #prints the list of items in queue
        return(str(self.items)) 

    def enqueue(self,i): 
        self.items.append(i)
        
    def dequeue(self): 
        if self.is_empty():
            return None 
        m=self.search()
        if m==None:
           return None
        else:
            self.items.remove(m)
            return m
    def search(self):
        x=None
        for i in self.items:
            if x==None:
                x=i
            elif i<x:
                x=i
        return(x)


# q=PriorityQueueList()
# q.enqueue(13)
# q.enqueue(10)
# q.enqueue(15)
# q.enqueue(29)
# q.enqueue(7)
# print(q.dequeue())
# print(q)