###############################
# Stack: LIFO, using array
###############################
class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_out_stack(self):
        if len(self.items) == 0:
            print("Nothing in stack")
        else:
            for item in self.items: print(item)



###################################################
# Test 

stack = Stack()
stack.print_out_stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Pass" if (stack.size() == 5) else "Fails")
stack.push(5)
stack.print_out_stack()
print("Pass" if (stack.size() == 5) else "Fails")

print("Pass" if (stack.pop() == 5) else "Fails")
print("Pass" if (stack.pop() == 4) else "Fails")

stack.print_out_stack()