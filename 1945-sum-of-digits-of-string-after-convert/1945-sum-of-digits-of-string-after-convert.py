class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ''
        for letter in s:
            res += str(ord(letter) - 96)
        for _ in range(k):
            res = sum(map(int,res))
            res = str(res)
        return int(res)