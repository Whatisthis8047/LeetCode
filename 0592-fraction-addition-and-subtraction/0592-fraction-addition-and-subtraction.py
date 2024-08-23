class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = []
        den = []
        left, right, res = 0, 0, 0
        is_num = 1
        while left < len(expression):
            if expression[right] == '/' and is_num:
                num.append(expression[left:right])
                left = right
                is_num = 0
            elif (expression[right] == '+' or expression[right] == '-') and (not is_num):
                den.append(expression[left+1:right])
                left = right
                is_num = 1
            elif right == len(expression)-1:
                den.append(expression[left+1:])
                break
            right += 1
        
        cm = self._CM(den)
        for i in range(len(num)):
            res += int(int(num[i])*(cm/int(den[i])))
        gcd_num = abs(self._gcd(res, cm))
        return f'{int(res/gcd_num)}/{int(cm/gcd_num)}'
    
    def _gcd(self, a, b):
        if a == 0:
            return b
        return self._gcd(b % a, a)

    def _CM(self, nums_list: list):
        res = 1
        for number in nums_list:
            res *= int(number)
        return res