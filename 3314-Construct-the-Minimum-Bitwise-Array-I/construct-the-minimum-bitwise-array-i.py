from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num == 2:
                ans.append(-1)
                continue
            for k in range(1, 32):
                if (num >> k) & 1 == 0:
                    ans.append(num - (1 << (k - 1)))
                    break
        return ans
        