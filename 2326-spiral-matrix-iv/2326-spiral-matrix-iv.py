# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # spiral matrix tend to follow the walls that closes after filling the line
        res = [[-1]*n for _ in range(m)]
        row, col = 0, 0
        edge = 0
        min_m, min_n = 1, 0
        while head:
            if edge == 0:
                # 0,0 to 0,n
                if col >= n-1:
                    res[row][col] = head.val
                    row += 1
                    n -= 1
                    edge += 1
                else:
                    res[row][col] = head.val
                    col += 1

            elif edge == 1:
                # 0,n to m,n
                if row >= m-1:
                    res[row][col] = head.val
                    col -= 1
                    m -= 1
                    edge += 1
                else:
                    print(row, col)
                    res[row][col] = head.val
                    row += 1
            
            elif edge == 2:
                # m,n to m,0
                if col <= min_n :
                    res[row][col] = head.val
                    row -= 1
                    min_n += 1
                    edge += 1
                else:
                    res[row][col] = head.val
                    col -= 1 

            elif edge == 3:
                # m,0 to 1,0
                if row <= min_m :
                    res[row][col] = head.val
                    col += 1
                    min_m += 1
                    edge = 0
                else:
                    res[row][col] = head.val
                    row -= 1
            head = head.next
            
        return res