class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        neg_num = 0
        min_abs = float('inf')  # Initialize to infinity
        abs_sum = 0

        for row in range(len(matrix)):
            for col in range(len(matrix)):
                if matrix[row][col] < 0:
                    neg_num += 1
                abs_num = abs(matrix[row][col])
                min_abs = min(min_abs, abs_num)
                
                abs_sum += abs_num

        if neg_num % 2 == 0:
            return abs_sum
        else:
            return abs_sum - (2 * min_abs)
        