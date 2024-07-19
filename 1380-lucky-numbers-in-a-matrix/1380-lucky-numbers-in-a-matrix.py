class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        col_max = [max(x) for x in zip(*matrix)]
        row_min = [min(x) for x in matrix]
        
        return set(col_max).intersection(row_min)