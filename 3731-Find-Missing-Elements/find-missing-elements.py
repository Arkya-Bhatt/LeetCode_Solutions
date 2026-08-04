from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        mn, mx = min(nums), max(nums)
        ans = []
        for x in range(mn + 1, mx):
            if x not in s:
                ans.append(x)
        return ans
        