from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if x == 2:
                res.append(-1)
                continue
            d = 1
            while (x & d) != 0:
                d <<= 1
            ans = x ^ (d >> 1)
            res.append(ans)
        return res
        