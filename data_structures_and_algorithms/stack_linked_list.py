################################
# Stack: LIFO, using linked list
################################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_nodes = 0

    def push(self, value):
        new_node = Node(value)
        
        if self.head is not None:
            new_node.next = self.head

        self.head = new_node
        self.num_nodes += 1
        
    def pop(self):
        if self.head == None:
            return None

        pop_node = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return pop_node

    def print_out_stack(self):
        if self.head == None:
            print("None")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
            


###################################################
# Test 

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.num_nodes == 5) else "Fails")
stack.push(5)
stack.print_out_stack()
print("Pass" if (stack.num_nodes == 5) else "Fails")

print("Pass" if (stack.pop() == 5) else "Fails")
print("Pass" if (stack.pop() == 4) else "Fails")

stack.print_out_stack()
