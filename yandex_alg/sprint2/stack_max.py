class StackMax:
    def __init__(self):
        self.items = []
    
    def push(self, x):
        self.items.append(x)
    
    def pop(self):
        if len(self.items) != 0:
            self.items.pop()
        else:
            print('error')
    
    def get_max(self):
        if len(self.items) != 0:
            print(max(self.items))
        else:
            print('None')

stack = StackMax()

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
