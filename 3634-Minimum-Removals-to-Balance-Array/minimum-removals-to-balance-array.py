from typing import List
from bisect import bisect_right

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_keep = 1
        for i in range(n):
            right = bisect_right(nums, k * nums[i])
            max_keep = max(max_keep, right - i)
        return (n - max_keep)
        