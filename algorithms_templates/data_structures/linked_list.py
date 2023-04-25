class Node:
    """Класс узла связанного списка."""

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """Класс инициирует экземпляр связанного списка."""

    def __init__(self, head=None):
        self.head = head


    def print_llist(self):
        temp = self.head
        while temp:
            print(temp.value, end='->')
            temp = temp.next
        print(None)


    def add_node(self, value):
        new_node = Node(value, None)
        temp = self.head
        if temp is None:
            self.head = new_node
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node


    def del_node_forward(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None


    def del_node_backward(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        temp = temp.next
        self.head = temp


ll_list = LinkedList()
