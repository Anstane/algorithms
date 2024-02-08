from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head # Инициируем голову

        while list1 and list2:
            if list1.val < list2.val: # Если list1.val меньше -> берём его, list1 = list1.next
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        current.next = list1 or list2 # Если что-то осталось в LL просто добавляем это
        return head.next


list1 = ListNode(1, ListNode(2 , ListNode(4)))
list2 = ListNode(1, ListNode(3 , ListNode(4)))

solution = Solution()
result = solution.mergeTwoLists(list1, list2)

while result:
    print(result.val, end='')
    result = result.next
