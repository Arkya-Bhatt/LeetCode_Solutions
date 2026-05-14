from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums) - 1
        if nums[-1] != n:
            return False
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False
        return nums[n - 1] == n
        