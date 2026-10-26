class Solution:
    def getBiggestThree(self, grid: list[list[int]]) -> list[int]:
        m,n = len(grid), len(grid[0])
        sums = set()
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j]) #add the 0 radius one
                r = 1 #radius for every possible center
                while i - r >= 0 and i + r < m and j - r>=0 and j + r < n:
                    curr_sum = 0
                    x,y = i - r, j #at top vertice

                    for _ in range(r): #to right vertice
                        curr_sum += grid[x][y]
                        x += 1 
                        y += 1

                    for _ in range(r): #to bottom vertice
                        curr_sum += grid[x][y]
                        x += 1 
                        y -= 1

                    for _ in range(r): #to left vertice
                        curr_sum += grid[x][y]
                        x -= 1 
                        y -= 1

                    for _ in range(r): #to top vertice
                        curr_sum += grid[x][y]
                        x -= 1 
                        y += 1

                    sums.add(curr_sum)
                    r += 1 #exapnd radius
            
        return sorted(list(sums), reverse = True)[:3]