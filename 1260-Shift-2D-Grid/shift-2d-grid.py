from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total
        ans = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                idx = r * n + c
                new_idx = (idx + k) % total
                nr, nc = divmod(new_idx, n)
                ans[nr][nc] = grid[r][c]
        return ans
        