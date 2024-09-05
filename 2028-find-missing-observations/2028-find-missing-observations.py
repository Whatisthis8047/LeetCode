class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # brute search
        total = mean * (len(rolls) + n)
        n_rolls = total - sum(rolls)

        if n_rolls > 6*n or n_rolls < n : return []

        avg = n_rolls//n 
        res = [avg] * n
        remain = n_rolls - (avg*n)
        if remain > 0:
            over = 6 - avg
            add = remain//over
            res = res[add:] + [6]*add
            final = remain%over
            res[0] += final
        return res


        