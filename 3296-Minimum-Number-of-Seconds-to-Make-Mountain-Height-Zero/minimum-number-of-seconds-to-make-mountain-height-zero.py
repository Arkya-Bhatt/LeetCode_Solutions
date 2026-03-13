from typing import List

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def can_finish(s: int) -> bool:
            total = 0
            for t in workerTimes:
                k = int((-1 + (1 + 8 * s / t) ** 0.5) / 2)
                total += k
                if total >= mountainHeight:
                    return True
            return total >= mountainHeight
        lo, hi = 1, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        while lo < hi:
            mid = (lo + hi) // 2
            if can_finish(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
        