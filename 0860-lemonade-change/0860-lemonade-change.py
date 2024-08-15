class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d5, d10 = 0, 0
        for cash in bills:
            if cash == 5:
                d5 += 1
            elif cash == 10:
                if d5 < 1:
                    return False
                d5 -= 1
                d10 += 1
            elif cash == 20:
                if d10 >= 1 and d5 >= 1:
                    d5 -= 1
                    d10 -= 1
                    continue
                elif d5 >= 3:
                    d5 -= 3
                    continue
                return False
        return True
                
