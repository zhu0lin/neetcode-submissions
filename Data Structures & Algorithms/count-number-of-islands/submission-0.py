from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        # while q:
        #     r, c = q.popleft()

        #     for dr, dc in directions:
        #         new_r = r + dr
        #         new_c = c + dc

        #         if (new_r >= 0 and new_r < rows) and (new_c >= 0 and new_c < cols) and (grid[new_r][new_c] == 1) and visited[new_r][new_c] == False:
        #             visited[new_r][new_c] = True
        #             q.append((new_r, new_c))
        #             islands += 1
        def bfs(r, c):

            q = deque()
            q.append((r, c))
            grid[r][c] = "0"
            
            while q:
                curr_r, curr_c = q.popleft()
                for dr, dc in directions:
                    new_r = curr_r + dr
                    new_c = curr_c + dc
                    
                    if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols or grid[new_r][new_c] == "0":
                        continue

                    q.append((new_r, new_c))
                    grid[new_r][new_c] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands


