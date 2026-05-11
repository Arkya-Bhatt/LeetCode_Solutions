from typing import List

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            for d in str(n):
                res.append(int(d))
        return res
        