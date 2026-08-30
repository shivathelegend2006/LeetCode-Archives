import collections

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        #perofrm bfs keep trakc of groups of 1 
        #whe it sees group brokedn resre count to 0 after comparing ity with the max count and replacing 

        if not grid:
            return 0
            
        ROWS, COLS = len(grid), len(grid[0])
        visited = set() 
        max_record = 0
        

        def bfs(r, c):
            q = collections.deque([(r, c)])
            visited.add((r, c))
            current_count = 0
            
            # Up, Down, Right, Left
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            
            while q:
                row, col = q.popleft()
                current_count += 1
                

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited):
                        
                        q.append((nr, nc))
                        visited.add((nr, nc)) 
                        
            return current_count


        for r in range(ROWS):
            for c in range(COLS):
         
                if grid[r][c] == 1 and (r, c) not in visited:
                    island_area = bfs(r, c)
                    max_record = max(max_record, island_area)
                    
        return max_record