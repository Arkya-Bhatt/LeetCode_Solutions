from typing import List
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_bounds = defaultdict(lambda: [float('inf'), -float('inf')])
        col_bounds = defaultdict(lambda: [float('inf'), -float('inf')])
        for r, c in buildings:
            row_bounds[r][0] = min(row_bounds[r][0], c)
            row_bounds[r][1] = max(row_bounds[r][1], c)
            col_bounds[c][0] = min(col_bounds[c][0], r)
            col_bounds[c][1] = max(col_bounds[c][1], r)
        ans = 0
        for r, c in buildings:
            minC, maxC = row_bounds[r]
            minR, maxR = col_bounds[c]
            if minC < c < maxC and minR < r < maxR:
                ans += 1
        return ans
        