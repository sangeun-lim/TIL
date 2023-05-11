class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 전가산기 구현
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            total = 0
            # 두 입력값의 합 계산
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(total + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next