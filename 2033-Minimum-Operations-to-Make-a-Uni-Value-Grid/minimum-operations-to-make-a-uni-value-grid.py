from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = []
        for row in grid:
            flat.extend(row)
        flat.sort()
        
        target = flat[len(flat) // 2]
        ops = 0
        for val in flat:
            if (val - target) % x != 0:
                return -1
            ops += abs(val - target) // x
        return ops
        