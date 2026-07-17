from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        MAX_BIT = 30
        ans = 0
        n = len(nums)
        for i in range(MAX_BIT):
            ones = sum((num >> i) & 1 for num in nums)
            zeros = n - ones
            ans += ones * zeros
        return ans
        