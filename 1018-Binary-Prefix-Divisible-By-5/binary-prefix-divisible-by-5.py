from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        curr = 0
        for b in nums:
            curr = (curr * 2 + b) % 5
            ans.append(curr == 0)
        return ans
        