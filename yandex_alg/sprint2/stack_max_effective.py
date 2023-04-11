class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.max_items = []
    
    def push(self, x):
        self.items.append(x)
        if not self.max_items or x >= self.max_items[-1]:
            self.max_items.append(x)
    
    def pop(self):
        if len(self.items) != 0:
            item_del = self.items.pop()
            if item_del == self.max_items[-1]:
                self.max_items.pop()
        else:
            print('error')
    
    def get_max(self):
        if len(self.items) != 0 and len(self.max_items) != 0:
            print(self.max_items[-1])
        else:
            print('None')

stack = StackMaxEffective()

n = int(input())
array = [input().split(' ') for i in range(n)]

new_array = []
for i in array:
    new_array.extend(i)

for j in range(len(new_array)):
    if new_array[j] == 'push':
        stack.push(int(new_array[j + 1]))
    if new_array[j] == 'get_max':
        stack.get_max()
    if new_array[j] == 'pop':
        stack.pop()
