from typing import List
from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = Counter(nums)
        n = len(nums) // 2
        for k, v in counter.items():
            if v == n:
                return k
        