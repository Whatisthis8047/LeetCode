# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        res = ListNode()

        while head:
            if head.val in nums:
                head = head.next

            else:
                if res.val == 0:
                    res.val = head.val
                    temp = res

                else:
                    temp.next = ListNode(head.val)
                    temp = temp.next
                    

                head = head.next

        return res

        # 초기화 res = ListNode(0, None)
        # 

        # res.next = ListNode(0, None)
        # [res.next].next = ListNode(0, None)
        # [res.next].next.next = ListNode(0, None)
        # ...
        