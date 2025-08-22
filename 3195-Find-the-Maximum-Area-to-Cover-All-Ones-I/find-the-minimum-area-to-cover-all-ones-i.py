from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        top, bottom = float("inf"), -float("inf")
        left, right = float("inf"), -float("inf")

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)

        if top == float("inf"):
            return 0

        height = bottom - top + 1
        width = right - left + 1
        return height * width
        