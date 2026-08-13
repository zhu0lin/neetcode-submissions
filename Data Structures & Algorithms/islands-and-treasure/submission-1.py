from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        grid[i][j] is either -1 (water, cannot be traversed), 0 (treasure)
        or 2147483647 (land)

        for each 2147483647 (land mass), we must find the shortest path
        to 0 (treasure)
        this seems like a shortest path problem.
        try to implement dijkstra's here?
        """
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        dist = 0

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append(([r, c]))
                    visit.add((r, c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
                
        