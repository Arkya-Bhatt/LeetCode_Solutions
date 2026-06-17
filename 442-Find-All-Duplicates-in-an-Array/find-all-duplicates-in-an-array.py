from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            idx = abs(num) - 1
            nums[idx] *= -1
            if nums[idx] > 0:
                ans.append(abs(num))
        return ans
        