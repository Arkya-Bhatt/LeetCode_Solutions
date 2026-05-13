from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            x, y = min(nums[i], nums[n - 1 - i]), max(nums[i], nums[n - 1 - i])
            diff[2] += 2
            diff[x + 1] -= 2
            diff[y + limit + 1] += 2
            diff[2 * limit + 1] -= 2
            diff[x + 1] += 1
            diff[x + y] -= 1
            diff[x + y + 1] += 1
            diff[y + limit + 1] -= 1
        res, cur = float('inf'), 0
        for s in range(2, 2 * limit + 1):
            cur += diff[s]
            res = min(res, cur)
        return res
        