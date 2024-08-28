class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):
            if 0 <= row < m and 0 <= col < n and grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row-1,col)
                dfs(row,col-1)
                dfs(row+1,col)
                dfs(row,col+1)
  
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    res += 1
                    dfs(row, col)
        return res
