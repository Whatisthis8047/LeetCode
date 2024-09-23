class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, s_dict = len(s), set(dictionary)
        @cache
        def dp(start):
            if start == n:
                return 0
            res = dp(start + 1) + 1
            for end in range(start, n):
                cur = s[start:end +1]
                if cur in s_dict:
                    res = min(res, dp(end + 1))
            return res
        
        return dp(0)