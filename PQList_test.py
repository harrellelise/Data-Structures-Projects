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
        work=0
        if self.is_empty():
            return None 
        m, work=self.search()
        if m==None:
           work+=1
           return None
        else:
            self.items.remove(m)
            work+=1
            return work
    def search(self):
        work=0
        x=None
        for i in self.items:
            work+=1
            if x==None:
                x=i
                work+=1
            elif i<x:
                x=i
                work+=1
        return(x, work)


# q=PriorityQueueList()
# q.enqueue(13)
# q.enqueue(10)
# q.enqueue(15)
# q.enqueue(29)
# q.enqueue(7)
# print(q.dequeue())
# print(q)