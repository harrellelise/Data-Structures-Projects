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
        work=0
        #if list is empty return none
        if self.is_empty():
            work+=1
            return None 
        #searches the list for the highest-priority item and removes it from wherever it is
        else:
            #searches for highest priority and returns highest priority node and node behind and in front of it
            f,c,b,work=self.search()
            work+=1
            #assign the highest priority variable to bye variable to return at the end
            bye=c.get_data()
            work+=1
            #if the node in front of highest priority is None, set the front node to the node behind the highest priority
            if f==None:
                work+=1
                self._front=b
            #if node behind is none, set rear to front and set next of f to None
            elif b==None:
                work+=1
                self._rear=f
                f.set_next(None)
            #the pointers to the nodes around it so the list doesn’t break
            else:
                work+=1
                f.set_next(b)
            #set length to -1
            self._length -= 1
            work+=1
            #return removed node
            return work
        
    #searches for highest priority node
    def search(self):
        work=0
        #get the front node's data and assign to x
        x=self._front.get_data()
        work+=1
        #create variables for the highest priority node and its front and back
        front=None
        n=None
        back=None
        work+=3
        #create variable to keep track of the node before the current one
        before=None
        work+=1
        #create variable next to keep track of the current node
        next=self._front
        work+=1
        #while next is not none
        while next!=None:
            #set variable v to data of current node
            v=next.get_data()
            work+=1
            #if current node is smaller than x, set to highest priority node
            if v<=x:
                x=v
                #keeps track of node before highest priority
                front=before
                #keeps track of highest priority node
                c=next
                #keeps track of node after highest priority
                back=next.get_next()
                work+=4
            #keeps track of node before next
            before=next
            work+=1
            #gets the next node
            next=next.get_next()
            work+=1
        #return highest priority and its front and back
        return (front, c, back, work)
    


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