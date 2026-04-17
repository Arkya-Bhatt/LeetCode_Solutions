from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        result = []
        for x in nums2:
            if count1[x] > 0:
                result.append(x)
                count1[x] -= 1
        return result
        