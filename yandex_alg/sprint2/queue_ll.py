class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self, tail=None):
        self.tail = tail
        self.head = tail
        self.queue_size = 0
    
    """Создаём ноду в конце списка."""
    def put(self, x):
        if self.tail != None:
            current = self.tail
            new_node = Node(x)
            current.next = new_node
            self.tail = new_node
            if self.head == None:
                self.head = new_node
        else:
            new_node = Node(x)
            self.tail = new_node
            self.head = new_node
        self.queue_size += 1

    """Удаляем и читаем ноду из начала спика."""
    def get(self):
        if self.head != None:
            if self.head.next is not None:
                print(self.head.value)
                current = self.head
                current = current.next
                self.head = current
                self.queue_size -= 1
            else:
                print(self.head.value)
                self.head = None
                self.queue_size -= 1
        else:
            print('error')

    """Возвращаем размер списка."""
    def size(self):
        print(self.queue_size)

queue = Queue()

n = int(input())
array = [input().split(' ') for i in range(n)]

new_array = []
for i in array:
    new_array.extend(i)

for j in range(len(new_array)):
    if new_array[j] == 'put':
        queue.put(int(new_array[j + 1]))
    if new_array[j] == 'get':
        queue.get()        
    if new_array[j] == 'size':
        queue.size()
