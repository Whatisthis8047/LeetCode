class Solution:
    def findComplement(self, num: int) -> int:
        blength = num.bit_length()
        mask = (1 << blength) - 1
        return num ^ mask