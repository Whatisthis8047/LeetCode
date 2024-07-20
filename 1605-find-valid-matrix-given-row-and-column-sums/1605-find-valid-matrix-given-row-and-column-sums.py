class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]
        
        for row in range(m):
            for col in range(n):
                min_val = min(rowSum[row], colSum[col])
                matrix[row][col] = min_val
                
                rowSum[row] -= min_val
                colSum[col] -= min_val
        
        return matrix


                    