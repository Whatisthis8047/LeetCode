class Solution:
    def maxScore(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            left = s[:i+1].count('0')
            right = s[i+1:].count('1')
            temp = left + right
            res = max(temp, res)

        return res