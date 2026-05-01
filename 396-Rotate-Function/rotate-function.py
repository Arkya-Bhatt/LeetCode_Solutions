from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        f = sum(i * x for i, x in enumerate(nums))
        ans = f
        n = len(nums)
        for k in range(1, n):
            f = f + total - n * nums[n - k]
            ans = max(ans, f)
        return ans
        