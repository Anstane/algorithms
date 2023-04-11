# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item

def solution(node, elem):
    # Your code
    # ヽ(´▽`)/
    # node = head elem = node2.value
    # print(node.value, elem) -> node0 node2
    idx = 0
    if node.value != None:
        try :
            while node.value != elem:
                node = node.next_item
                idx += 1
        except Exception:
            idx = -1
    return idx

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2

if __name__ == '__main__':
    test()