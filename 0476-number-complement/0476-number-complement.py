class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        res = ""
        for bit in bin_num:
            if bit == '0':
                res += '1'
            else:
                res += '0'
        return int(res, 2)