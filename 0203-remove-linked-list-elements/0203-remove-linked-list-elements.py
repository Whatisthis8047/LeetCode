# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None

        res = ListNode()
        temp = res
        while head.next:
            if head.val == val:
                head = head.next
                continue
            temp.next = ListNode(head.val)
            temp = temp.next
            head = head.next

        return res.next
        