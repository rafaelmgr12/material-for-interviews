"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r,c = row +dr, col + dc
                    if ((r) in range(rows) and
                        (c) in range(cols) and
                        grid[r][c] == '1' and
                        (r,c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c ) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands

    def numIslands2(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    self.dfs(grid, r, c, visited)
                    islands += 1
        return islands
    def dfs(self, grid, r, c, visited):
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0' or (r, c) in visited:
            return
        visited.add((r, c))
        self.dfs(grid, r+1, c, visited)
        self.dfs(grid, r-1, c, visited)
        self.dfs(grid, r, c+1, visited)
        self.dfs(grid, r, c-1, visited)
        return