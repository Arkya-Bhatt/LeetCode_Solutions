from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0
        for x in arr:
            prev = min(prev + 1, x)
        return prev
        