class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#comment
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    
    def delete(self, task_name):
        if not self.head:
            return None
        if self.head.data["name"] == task_name:
            removed = self.head.data
            self.head = self.head.next
            return removed
        current = self.head
        while current.next:
            if current.next.data["name"] == task_name:
                removed = current.next.data
                current.next = current.next.next
                return removed
            current = current.next
        return None



    

