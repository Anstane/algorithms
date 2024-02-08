class MyHashMap:

    def __init__(self):
        self.array_point = []
        self.hash_map = []

    def put(self, key: int, value: int) -> None:
        self.array_point.append(key)
        self.array_point.append(value)

        for i in range(len(self.hash_map)):
            if self.hash_map[i][0] == self.array_point[0]:
                self.hash_map[i] = self.array_point
                self.array_point = []
            
        if len(self.array_point) != 0:
            self.hash_map.append(self.array_point)
            self.array_point = []
            
        print(self.hash_map)

    def get(self, key: int) -> int:
        hash_value = 0
        for i in range(len(self.hash_map)):
            if self.hash_map[i][0] == key:
                hash_value += self.hash_map[i][1]
                print(hash_value)

        if hash_value == 0:
            print(-1)

    def remove(self, key: int) -> None:
        for i in range(len(self.hash_map)):
            if self.hash_map[i][0] == key:
                self.hash_map.pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

obj = MyHashMap()

obj.remove(2)
obj.put(3, 11)
obj.put(4, 13)
obj.put(15, 6)
obj.put(6, 15)
obj.put(8, 8)
obj.put(11, 0)
obj.get(11)
obj.put(1, 10)
obj.put(12, 14)


class ListNode: # Создаём LL
    def __init__(self, key, value): # Инициируем ноду
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = [None] * self.size # Заведомо делаем массим на 1000 элементов

    def _index(self, key: int) -> int: # Функация для получения индекса записи
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self._index(key) # Получаем индекс
        if not self.table[idx]: # Если индекс не в массиве
            self.table[idx] = ListNode(key, value)
            return # Просто запихиваем его
        current = self.table[idx]
        while current:
            if current.key == key:
                current.value = value # Перезаписываем, если есть в LL
                return
            if not current.next:
                current.next = ListNode(key, value) # Создаём новую - если дошли до конца
                return
            current = current.next

    def get(self, key: int) -> int:
        idx = self._index(key)
        current = self.table[idx]
        while current: # Как в обычном LL итерируем до самого конца - пусто - return -1
            if current.key == key:
                return current.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        idx = self._index(key)
        current = self.table[idx]
        if not current:
            return
        if current.key == key:
            self.table[idx] = current.next
            return
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next