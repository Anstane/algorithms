from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        while l1 or l2 or carry:
            x = l1.val if l1 else 0 # 2 4 3
            y = l2.val if l2 else 0 # 5 6 4
            _sum = x + y + carry # 7 8
            carry = _sum // 10 # 1 0
            current.next = ListNode(_sum % 10) # 7 0 8
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next


l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# To print the result
while result:
    print(result.val)
    result = result.next
