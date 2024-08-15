class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0}
        for cash in bills:
            if cash == 5:
                change[5] += 1
            elif cash == 10:
                change[10] += 1
                if change[5] < 1:
                    return False
                change[5] -= 1
            elif cash == 20:
                change[20] += 1
                if change[10] < 1 or change[5] < 1:
                    if change[5] >= 3:
                        change[5] -= 3
                        continue
                    return False
                change[5] -= 1
                change[10] -= 1
        return True
