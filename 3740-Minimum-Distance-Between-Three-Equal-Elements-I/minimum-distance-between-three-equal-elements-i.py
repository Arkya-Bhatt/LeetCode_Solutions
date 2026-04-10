from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        min_dist = float("inf")
        for i, num in enumerate(nums):
            ind = pos[num]
            if len(ind) >= 2:
                a, b = ind[-2], ind[-1]
                dist = abs(a - b) + abs(b - i) + abs(i - a)
                min_dist = min(min_dist, dist)
            pos[num].append(i)
        return min_dist if min_dist != float("inf") else -1
        