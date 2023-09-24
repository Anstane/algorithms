from collections import deque


graph = {}
graph["you"] = [ "alice", "bob", "claire"] 
graph["bob"] = ["anuj", "peggy"] 
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"] 
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    search_queue = deque() # С помощью дека делам очередь
    search_queue += graph[name] # Запихиваем граф в эту очередь
    searched = [] # Список уже проверенных
    while search_queue: # Пока в очереди кто-то есть
        person = search_queue.popleft() # Берём человека с левого края
        if not person in searched: # Если человек не был ещё затронут
            if person == 'rand_name': # Проверка
                print(f'{person} нашлась.')
                return True
            else: # Если это не тот человек - берём следующего 
                search_queue += graph[person] # Добавляем связи следующего человека в граф
                searched.append(person) # Искомого в список проверенных
    return False # Никого не нашли

search("you")
