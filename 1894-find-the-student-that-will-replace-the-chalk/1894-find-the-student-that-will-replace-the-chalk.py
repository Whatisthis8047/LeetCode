class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        total = sum(chalk)

        if total <= k:
            k = k % total
        while True:
            for i in range(n):
                if k < chalk[i]:
                    return i
                k -= chalk[i]