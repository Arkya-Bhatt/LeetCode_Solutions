from typing import List
from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)
        for indices in pos.values():
            k = len(indices)
            total = sum(indices)
            prevSum = 0
            for l, i in enumerate(indices):
                left = (l * i) - prevSum
                right = (total - prevSum - i) - (k - l - 1) * i
                ans[i] = left + right
                prevSum += i
        return ans
        