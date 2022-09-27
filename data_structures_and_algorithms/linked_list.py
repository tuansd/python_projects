
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return

        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Appended new Node with value:", node.next.value)
    
    # delete last node
    def pop(self):
        if self.head is None:
            print("List is empty")
            return None
        elif self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        else:
            prev = current = self.head

            while(current.next is not None):
                prev = current
                current = current.next
            
                
            value = current.value
            prev.next = None
            return value
    
    # print out list
    def show_list(self):
        print("List: ")
        if self.head is None:
            print("List is empty")            
        else:
            current = self.head
            prev = None
            while(current is not None):
                print(current.value)                
                current = current.next
                
            
####################################
# Test

llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")
llist.append("Fourth Node")
llist.append("Fifth Node")
print("--------------")
print("Delete: ", llist.pop())
print("Delete: ", llist.pop())
print("Delete: ", llist.pop())
print("--------------")

llist.show_list()


