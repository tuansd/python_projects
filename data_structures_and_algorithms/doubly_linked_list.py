# DoublyLinkedList

# Node Class: value, next, prev
class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# DoublyLinkedList: head, tail, length
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0        # extra

    # Insert node at the end of list
    def append(self,value):
        new_node = DoubleNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node            
            self.head.next = self.tail
            print("Head Node created: ", self.head.value)
        else:
            new_node.prev = self.tail
            self.tail.next = new_node 
            self.tail = new_node # new tail in DoublyLinkedList
            print("Appended new Node with value:", self.tail.value)
        self.length += 1        
        return True

    # show all nodes in list
    def print_llist(self):
        print("List: ")
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    # delete node at the end of the list
    def pop(self):
        if self.head is None:
            print("None")
            return False
        elif self.head is self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length = 0
            return value
        else:
            value = self.tail.value
            temp = self.tail.prev
            
            self.tail = temp
            self.tail.next = None
            
            self.length -= 1
            return value        
# End class

###########################################
# Running Test

# dllist = DoublyLinkedList()
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)
# dllist.append(5)
# print("--------------")
# print("Delete: ", dllist.pop())
# print("Delete: ", dllist.pop())
# print("--------------")
# dllist.print_llist()



dllist = DoublyLinkedList()
dllist.append("First Node")
dllist.append("Second Node")
dllist.append("Third Node")
dllist.append("Fourth Node")
dllist.append("Fifth Node")
print("--------------")
print("Delete: ", dllist.pop())
print("Delete: ", dllist.pop())
print("--------------")
dllist.print_llist()
