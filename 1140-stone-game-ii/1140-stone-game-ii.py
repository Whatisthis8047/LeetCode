class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # todo- Study with notetaking.
        dp = {}

        # return Alice's total
        def dfs(i, M):
            if (i, M) in dp:
                return dp[(i, M)]
            summ = sum(piles[i:])
            if i + 2 * M >= len(piles):
                return summ
            res = summ - min(dfs(i + X, max(M, X)) for X in range(1, 2 * M + 1))
            dp[(i, M)] = res
            return res

        return dfs(0, 1)