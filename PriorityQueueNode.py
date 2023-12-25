import Node
class PriorityQueueNode:
    
    def __init__(self):
        #initiate variables
        self._front = None
        self._rear  = None 
        self._length = 0 

    def enqueue(self,item):
        #add to the back of the queue -- the rear points to None
        node = Node.Node(item)
        #if it is empty set first node to front and back
        if self.is_empty():
            self._front = node 
            self._rear = node 
        #otherwise, set rear to the new node
        else:
            self._rear.set_next(node)
            self._rear = node
        #add one to length
        self._length += 1
            
    def dequeue(self):
        #if list is empty return none
        if self.is_empty():
            return None 
        #searches the list for the highest-priority item and removes it from wherever it is
        else:
            #searches for highest priority and returns highest priority node and node behind and in front of it
            f,c,b=self.search()
            #assign the highest priority variable to bye variable to return at the end
            bye=c.get_data()
            #if the node in front of highest priority is None, set the front node to the node behind the highest priority
            if f==None:
                self._front=b
            #if node behind is none, set rear to front and set next of f to None
            elif b==None:
                self._rear=f
                f.set_next(None)
            #the pointers to the nodes around it so the list doesn’t break
            else:
                f.set_next(b)
            #set length to -1
            self._length -= 1
            #return removed node
            return bye
        
    #searches for highest priority node
    def search(self):
        #get the front node's data and assign to x
        x=self._front.get_data()
        #create variables for the highest priority node and its front and back
        front=None
        n=None
        back=None
        #create variable to keep track of the node before the current one
        before=None
        #create variable next to keep track of the current node
        next=self._front
        #while next is not none
        while next!=None:
            #set variable v to data of current node
            v=next.get_data()
            #if current node is smaller than x, set to highest priority node
            if v<=x:
                x=v
                #keeps track of node before highest priority
                front=before
                #keeps track of highest priority node
                c=next
                #keeps track of node after highest priority
                back=next.get_next()
            #keeps track of node before next
            before=next
            #gets the next node
            next=next.get_next()
        #return highest priority and its front and back
        return (front, c, back)
    


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
    def size(self):
        return self._length

# pq = PriorityQueueNode()
# pq.enqueue(5)
# print(pq)
# pq.enqueue(7)
# print(pq)
# pq.enqueue(2)
# print(pq)
# pq.enqueue(6)
# print(pq)
# print(pq.dequeue())
# print(pq.dequeue())
# print(pq.dequeue())
# print(pq.dequeue())
# print(pq.dequeue())
# print(pq.dequeue())
# print(pq.size())