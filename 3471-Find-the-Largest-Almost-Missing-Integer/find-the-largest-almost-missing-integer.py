from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        from collections import Counter
        wndw_count = Counter()
        n = len(nums)
        for i in range(n - k + 1):
            wndw_vals = set(nums[i:i + k])
            for x in wndw_vals:
                wndw_count[x] += 1
        for x in range(50, -1, -1):
            if wndw_count[x] == 1:
                return x
        return -1
        