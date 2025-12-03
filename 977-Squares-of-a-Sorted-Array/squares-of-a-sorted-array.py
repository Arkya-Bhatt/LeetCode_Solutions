from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        k = n - 1
        while l <= r:
            left_sq = nums[l] * nums[l]
            right_sq = nums[r] * nums[r]
            if left_sq > right_sq:
                res[k] = left_sq
                l += 1
            else:
                res[k] = right_sq
                r -= 1
            k -= 1
        return res
        