class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        for ones in bin(start^goal)[2:]:
            res += int(ones)
        return res