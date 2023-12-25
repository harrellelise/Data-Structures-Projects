import BinaryHeap
import time
import random

random.seed(2007)

#re-initialize the data collection file
file = open("BinaryHeapData.csv","w")
file.write("operation, n, work\n")
file.close()

file = open("BinaryHeapData.csv","a") #open in append mode so the data isn't overwritten
for i in range(0,20): #we're going to run 20 experiments
    
    #create a random list of a random size
    bh = BinaryHeap.BinaryHeap()
    for i in range(random.randint(100000,1000000)):
        #fill the list with random integers
        bh.insert(random.randint(11,100000))
    
    #now that the heap is big, set up the tests and check how long it takes to insert a new item of high priority
    work = bh.insert(8)
    
    file.write("insert, "+str(bh.size())+", "+str(work)+"\n")
    print("inserted 8 into a heap with size "+str(bh.size()))
print("End binary heap insert\n")

file.close()

print("Done. check the file for your test results")