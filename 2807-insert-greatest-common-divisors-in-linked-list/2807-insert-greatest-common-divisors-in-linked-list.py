# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def GCD(num1, num2):
            if num1 < num2:
                num1, num2 = num2, num1
            while num2 != 0:
                num1, num2 = num2, num1%num2
            return num1
        
        cur = head
        nxt = head.next
        while nxt:
            gcd = GCD(cur.val, nxt.val)
            cur.next = ListNode(gcd, nxt)
            cur = nxt
            nxt = nxt.next
        return head