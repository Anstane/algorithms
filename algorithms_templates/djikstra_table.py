graph = {}
graph["start"] = {} # Начальная нода
graph["start"]["a"] = 6 # start -> a
graph["start"]["b"] = 2 # start -> b
graph["a"] = {} # Нода А
graph["a"]["fin"] = 1 # a -> fin
graph["b"] = {} # Нода B
graph["b"]["a"] = 3 # b -> a
graph["b"]["fin"] = 5 # b -> fin
graph["fin"] = {} # Финальная нода

infinity = float("inf")
costs = {} # Вес узлов - будет меняться по мере прохождения графа
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {} # Родительские узлы
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None 

processed = [] # Массив уже пройденых узлов


def find_the_lowest_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs: # Перебираем все ноды
        cost = costs[node] 
        if cost < lowest_cost and node not in processed: # Если это самый меньший узел и он не обработан
            lowest_cost = cost # Назначаем его новым минимумом
            lowest_cost_node = node
    return lowest_cost_node

node = find_the_lowest_node(costs) # Находим узел с наименьшей стоимостью
while node: # Пока все узлы не обработаны
    cost = costs[node] # Добавляем вес узлов
    neighbors = graph[node] # Переменная с соседями узла
    for n in neighbors.keys(): # Перебираем всех соседей узла
        new_cost = cost  + neighbors[n] # Если к соседу можно добраться быстрее
        if costs[n] > new_cost:
            costs[n] = new_cost # Обновляем стоимость узла
            parents[n] = node # Обновляем родительские узлы для соседей
    processed.append(node) # Отмечаем узел как обработанный
    node = find_the_lowest_node(costs) # Ищем следующий узел для обработки

print(costs, parents)
