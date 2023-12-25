import PQList_test
import PQNode_test
import time
import random


#test the list first
random.seed(2007)

#create the file
file=open("ListData.csv", "w")
file.write("operation, n, work\n")
file. close()

#open file in append mode
file= open("ListData.csv", "a")
#run 20 experiments
for i in range(0,20):
    #create random list of random size.
    pql=PQList_test.PriorityQueueList()
    for i in range(random.randint(100000,1000000)):
        #fill the list with random integers
        pql.enqueue(random.randint(2,100000))
    
    #set up tests to check how long it takes to remove a new item of high priority
    pql.enqueue(1)
    work=pql.dequeue()

    file.write("remove, " + str(pql.size())+ ", " + str(work)+ "\n")
    print("Removed the highest priority, '1', from a list-queue with size " + str(pql.size()))
print("End Priority Queue List Insert\n")

file.close()

print("Done. Check the file for your results")

#create the file
file=open("QueueData.csv", "w")
file.write("operation, n, work\n")
file.close()

#open it in append mode
file=open("QueueData.csv", "a")
#run the test 20 times
for i in range(0,20):
    pqn=PQNode_test.PriorityQueueNode()
    for i in range(random.randint(100000,1000000)):
        #add random amount of random numbers to the queue
        pqn.enqueue(random.randint(2,1000000))
    #add 1 to the end of the queue, as lowest number
    pqn.enqueue(1)
    #dequeue the highest priority
    work=pqn.dequeue()

    file.write("remove, " + str(pqn.size()) + ", " + str(work) + "\n")
    print("Removed the highest priority, '1', from a node-based-queue with size " + str(pqn.size()))
print("End Priority Queue Node Insert\n")

file.close()

print("Done. Check the file for your results")





