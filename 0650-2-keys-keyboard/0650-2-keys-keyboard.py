class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 2
        else:
            factors = []
            i = 2
            while i <= n:
                if n % i == 0:
                    factors.append(i)
                    n = n / i
                else:
                    i += 1

            if factors == []:
                return n
            else:
                return sum(factors)