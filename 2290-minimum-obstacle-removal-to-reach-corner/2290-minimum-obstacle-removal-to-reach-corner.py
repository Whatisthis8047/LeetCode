class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        min_obs = [[float('inf')] * n for _ in range(m)]
        min_obs[0][0] = 0
        queue = deque([(0, 0, 0)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            row, col, obs = queue.popleft()

            if obs > min_obs[row][col]:
                continue
                
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if (0 <= new_row < m and 0 <= new_col < n):
                    new_obs = obs + grid[new_row][new_col]
                    
                    if new_obs < min_obs[new_row][new_col]:
                        min_obs[new_row][new_col] = new_obs
                        queue.append((new_row, new_col, new_obs))
        
        return min_obs[m-1][n-1] if min_obs[m-1][n-1] != float('inf') else -1