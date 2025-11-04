from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n - k + 1):
            wndw = nums[i:i+k]
            freq = Counter(wndw)
            sorted_items = sorted(freq.items(), key=lambda v: (-v[1], -v[0]))
            kept_items = {item[0] for item in sorted_items[:x]}
            x_sum = sum(v for v in wndw if v in kept_items)
            res.append(x_sum)
        return res
             