from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        seen = [[False] * n for _ in range(m)]

        def dfs(i, j, px, py, letter):
            seen[i][j] = True
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                x, y = i + dx, j + dy
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if x == px and y == py:
                    continue
                if grid[x][y] != letter:
                    continue
                if seen[x][y]:
                    return True
                if dfs(x, y, i, j, letter):
                    return True
            return False

        for i in range(m):
            for j in range(n):
                if not seen[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True
        return False
        