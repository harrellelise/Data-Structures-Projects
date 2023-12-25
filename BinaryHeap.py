
class BinaryHeap:
    
    def __init__(self):
        self.heapList = [None]
        self.currentSize = 0
        
    def insert(self,k):
       work = 0
       self.heapList.append(k)
       work += 1
       self.currentSize += 1
       work += self.perc_up(self.currentSize)
       return work
       
    def perc_up(self,i):
        work = 0
        while i//2>0: 
            work += 1
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
                work += 3
            i = i//2
            work += 1
        return(work)

    def get_root(self):
        if self.isEmpty():
            return None #I added this; it wasn't in the book
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return (retval)
    
    def percDown(self,i):
        while(i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp 
            i = mc
        
    def minChild(self,i):
        if i*2 +1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def size(self):
        return self.currentSize
    
    def is_empty(self):
        return self.currentSize == 0    
            
    def __str__(self):
        return (str(self.heapList))