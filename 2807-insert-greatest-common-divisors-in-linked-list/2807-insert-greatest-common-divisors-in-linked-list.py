# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def GCD(num1, num2):
            if num1 == num2:
                return num1
            elif num1 > num2:
                for factor in range(num2, 0, -1):
                    if num1 % factor == 0 and num2 % factor == 0:
                        return factor
            elif num1 < num2:
                for factor in range(num1, 0, -1):
                    if num1 % factor == 0 and num2 % factor == 0:
                        return factor
        cur = head
        nxt = head.next
        while nxt:
            gcd = GCD(cur.val, nxt.val)
            cur.next = ListNode(gcd, nxt)
            cur = nxt
            nxt = nxt.next
        return head