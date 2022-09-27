################################
# Queue: FIFO, using linked list
################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def size(self):
        return self.num_nodes

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.num_nodes += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            dequeue_node_value = self.head.value
            self.head = self.head.next

        self.num_nodes -= 1
        return dequeue_node_value

    # print out list
    def show_queue(self):
        print("Queue: ")
        if self.head is None:
            print("List is empty")            
        else:
            current = self.head
            prev = None
            while(current is not None):
                print(current.value)                
                current = current.next

###################################################
# Test 

q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.show_queue()
print("Pass" if (q.size() == 3) else "Fails")
q.enqueue("d")
print("Pass" if (q.size() == 4) else "Fails")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")
print("Pass" if (q.size() == 2) else "Fail")

q.num_nodes = 1
print(q.num_nodes)
print("---------------------------")
q.show_queue()




            
