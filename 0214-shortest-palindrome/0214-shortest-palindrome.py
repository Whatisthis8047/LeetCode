class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def lps_table(s):
            lps = [0] * len(s)
            length = 0
            i = 1

            while i < len(s):
                if s[i] == s[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        rev_s = s[::-1]
        comb = s + '@' + rev_s
        lps = lps_table(comb)

        return rev_s[:len(s) - lps[-1]] + s
