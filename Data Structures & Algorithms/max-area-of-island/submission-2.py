from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        this is similar to number of islands.
        i think we can use BFS here too.
        """

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0

        def bfs(r, c):

            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            area = 0
            
            while q:
                curr_r, curr_c = q.popleft()
                area += 1
                for dr, dc in directions:
                    new_r = curr_r + dr
                    new_c = curr_c + dc
                    
                    if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols or grid[new_r][new_c] == 0:
                        continue

                    q.append((new_r, new_c))
                    grid[new_r][new_c] = 0
                    

            return area

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    print(area)
                    max_area = max(max_area, area)

        return max_area