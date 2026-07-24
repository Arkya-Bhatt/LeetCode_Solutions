from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        bits = 0
        x = n
        while x > 0:
            bits += 1
            x >>= 1
        return 1 << bits
        