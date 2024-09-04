class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_dir = 0 
        pos = [0, 0]  

        obstacle_set = set(map(tuple, obstacles))
        
        max_dis = 0
        
        for command in commands:
            if command == -2:  # Turn left
                current_dir = (current_dir - 1) % 4
            elif command == -1:  # Turn right
                current_dir = (current_dir + 1) % 4
            else:
                dx, dy = directions[current_dir]
                for _ in range(command):
                    new_pos = (pos[0] + dx, pos[1] + dy)
                    if new_pos in obstacle_set:
                        break  # obstacle encountered
                    pos[0], pos[1] = new_pos
                max_dis = max(max_dis, pos[0]**2 + pos[1]**2)
        
        return max_dis
