from typing import List

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        i = 0
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        if i == 0 or i == n - 1:
            return False
        peak_idx = i
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1
        if i == peak_idx or i == n - 1:
            return False
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        return i == n - 1
        