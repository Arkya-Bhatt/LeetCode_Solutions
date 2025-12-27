from typing import List

class Solution:
    def bs(self, n: int, t: int) -> int:
        l = 0
        r = len(n) - 1
        while l <= r:
            mid = (l + r) // 2
            if n[mid] > t:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def searchRange(self, nums: List[int], t: int) -> List[int]:
        start = self.bs(nums, t - 0.5)
        end = self.bs(nums, t + 0.5)
        if start == end:
            return [-1,-1]
        return [start, end-1]