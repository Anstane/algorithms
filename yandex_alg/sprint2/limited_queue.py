class MyQueueSized:
    def __init__(self, m):
        self.queue = [None] * m
        self.max_size = m
        self.head = 0
        self.tail = 0
        self.queue_size = 0

    def push(self, x):
        if self.queue_size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.queue_size += 1
        else:
            print("error")

    def pop(self):
        if self.queue_size == 0:
            print(None)
        else:
            x = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.queue_size -= 1
            print(x)

    def peek(self):
        if self.queue_size == 0:
            print(None)
        else:
            print(self.queue[self.head])
    
    def size(self):
        print(self.queue_size)

n = int(input())
m = int(input())

queue = MyQueueSized(m)

array = [input().split(' ') for i in range(n)]

new_array = []
for i in array:
    new_array.extend(i)

for j in range(len(new_array)):
    if new_array[j] == 'push':
        queue.push(int(new_array[j + 1]))
    if new_array[j] == 'pop':
        queue.pop()        
    if new_array[j] == 'peek':
        queue.peek()
    if new_array[j] == 'size':
        queue.size()
