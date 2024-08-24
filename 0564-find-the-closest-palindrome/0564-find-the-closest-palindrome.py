class Solution:
    def nearestPalindromic(self, n: str) -> str:
        len_n = len(n)
        i = len_n // 2 - 1 if len_n % 2 == 0 else len_n // 2
        first_half = int(n[: i + 1])

        cands = []
        cands.append(
            self._halfToPalindrom(first_half, len_n % 2 == 0)
        )
        cands.append(
            self._halfToPalindrom(first_half + 1, len_n % 2 == 0)
        )
        cands.append(
            self._halfToPalindrom(first_half - 1, len_n % 2 == 0)
        )
        cands.append(10 ** (len_n - 1) - 1)
        cands.append(10**len_n + 1)

        diff = float("inf")
        res = 0
        nl = int(n)
        for cand in cands:
            if cand == nl:
                continue
            if abs(cand - nl) < diff:
                diff = abs(cand - nl)
                res = cand
            elif abs(cand - nl) == diff:
                res = min(res, cand)
        return str(res)

    def _halfToPalindrom(self, half, is_even):
        res = half
        if not is_even:
            half = half // 10
        while half > 0:
            res = res * 10 + half % 10
            half = half // 10
        return res