from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        prev = float("-inf")
        for x in nums:
            assigned = max(x - k, prev + 1)
            if assigned <= x + k:
                ans += 1
                prev = assigned
        return ans
        