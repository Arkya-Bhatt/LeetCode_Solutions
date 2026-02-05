from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i, x in enumerate(nums):
            if x == 0:
                result.append(0)
            else:
                target = (i + x + n) % n
                result.append(nums[target])
        return result
        