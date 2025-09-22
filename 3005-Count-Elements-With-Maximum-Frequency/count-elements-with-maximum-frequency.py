from typing import List

from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count_dict = Counter(nums)
        max_freq = max(count_dict.values())
        res = 0
        for k, v in count_dict.items():
            if v == max_freq:
                res += v
        return res
