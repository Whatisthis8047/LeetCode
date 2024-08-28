class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def DFS(row, col):
            if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == "1":
                grid[row][col] = "0"

                DFS(row-1,col)
                DFS(row,col-1)
                DFS(row+1,col)
                DFS(row,col+1)

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    res += 1
                    DFS(row,col)
        return res