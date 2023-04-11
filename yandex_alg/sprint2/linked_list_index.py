# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item


def solution(node, idx):
    # Your code
    # ヽ(´▽`)/
    cur_node = node

    # Если индекс 0 - возвращаем следующий элемент
    if idx == 0:
        return cur_node.next_item
    
    count = 0
    while count != idx-1: # Ищем элемент предшествующий текущему
        cur_node = cur_node.next_item
        count += 1

    # Связываем напрямую предшествующий и следующий элементы
    cur_node.next_item = cur_node.next_item.next_item
    
    return node

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3

if __name__ == '__main__':
    test()