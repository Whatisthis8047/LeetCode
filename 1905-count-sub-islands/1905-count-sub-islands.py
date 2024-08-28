class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # need to check if all cells are contained in grid1 island
        m, n = len(grid2), len(grid2[0])
        res = 0
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid2[row][col] == 0:
                return True
            is_sub = grid1[row][col] == 1
            grid2[row][col] = 0
            
            is_sub = dfs(row-1, col) and is_sub
            is_sub = dfs(row+1, col) and is_sub
            is_sub = dfs(row, col-1) and is_sub
            is_sub = dfs(row, col+1) and is_sub
            
            return is_sub
        
        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1:
                    if dfs(row, col):
                        res += 1
        
        return res