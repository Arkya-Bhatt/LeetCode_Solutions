from typing import List
from collections import defaultdict

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        ans = float("inf")
        for lst in pos.values():
            if len(lst) < 3:
                continue
            for i in range(len(lst) - 2):
                a, b, c = lst[i], lst[i + 1], lst[i + 2]
                dist = 2 * (c - a)
                ans = min(ans, dist)
        return ans if ans != float("inf") else -1
