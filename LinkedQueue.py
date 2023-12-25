import Node 
class LinkedQueue:
    
    def __init__(self):
        self._front = None
        self._rear  = None 
        self._length = 0 
        
    def enqueue(self,item):
        #add to the back of the queue -- the rear points to None
        node = Node.Node(item)
        if self.is_empty():
            self._front = node 
            self._rear = node 
        else:
            self._rear.set_next(node)
            self._rear = node
        self._length += 1
            
    def dequeue(self):
        if self.is_empty():
            return None 
        else:
            f = self._front.get_data()
            self._front = self._front.get_next()
            self._length -= 1
            return f
            
    def __str__(self):
        s = ""
        next = self._front
        while next != None:
            s += str(next.get_data()) + " "
            next = next.get_next()
        return s

    def is_empty(self):
        if self._front == None:
            return True 
        return False

    

pq = LinkedQueue()
pq.enqueue(5)
print(pq)
pq.enqueue(7)
print(pq)
pq.enqueue(2)
print(pq)
pq.enqueue(6)
print(pq)
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
