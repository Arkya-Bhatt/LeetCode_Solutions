from typing import List
from math import inf

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = 0
        ans = -inf
        min_pref = [inf] * k
        min_pref[(k - 1) % k] = 0
        for i, x in enumerate(nums):
            s += x
            r = i % k
            if min_pref[r] < inf:
                ans = max(ans, s - min_pref[r])
            if s < min_pref[r]:
                min_pref[r] = s
        return ans
        