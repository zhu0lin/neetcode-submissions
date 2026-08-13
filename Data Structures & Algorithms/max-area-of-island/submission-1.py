class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Understand
        Input: An adjacency matrix grid where grid[i] is either a 0 (water)
        or a 1 (land). 
        Output: The area of the largest island

        Plan
        An island is defined as a group of 1s connected horizontally or vertically,
        but not diagonally. The area of an island is the num of cells within 
        the island.

        DFS Approach
        Iterate over all cells in grid
        Call DFS on each cell
        DFS function: Check if row/col out of bounds, if current cell is water (skip),
        and if we have already visited this cell (skip). 
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def dfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visited):
                return 0

            visited.add((r, c))
            return (1 + dfs(r-1, c) + dfs(r+1, c) + dfs(r, c-1) + dfs(r, c+1))

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area, dfs(r, c))

        return max_area
        