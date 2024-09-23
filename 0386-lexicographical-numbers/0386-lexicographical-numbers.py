class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lex_nums = []
        cur = 1
        for _ in range(n):
            lex_nums.append(cur)

            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur >= n:
                    cur //= 10
                cur += 1
        return lex_nums