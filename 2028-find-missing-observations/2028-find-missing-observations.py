class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # brute search
        total = mean * (len(rolls) + n)
        n_rolls = total - sum(rolls)
        res = []

        if (n_rolls / n > 6) or (n_rolls / n < 1) : return res

        for i in range(n):
            x = n_rolls // (n - i)
            res.append(x)
            n_rolls -= x
        
        return res