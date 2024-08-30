class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return sqrt(num) == round(sqrt(num))