class Node:
    def def __init__(self, data):
        self.data = data
        self.next = None

#comment
class LinkedList:
    def def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head

    

