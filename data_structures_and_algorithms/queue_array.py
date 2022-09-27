###############################
# Queue: FIFO, using array
###############################
class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(0)

    def show_queue(self):
        print(self.items)
        


###################################################
# Test 

q = Queue()
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.show_queue()
print("-------------------")

print("Pass" if (q.size() == 3) else "Fails")
q.enqueue("d")
print("Pass" if (q.size() == 4) else "Fails")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")
print("Pass" if (q.size() == 2) else "Fail")
q.show_queue()