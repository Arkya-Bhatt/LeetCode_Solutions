from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lst = []
        counter = Counter(nums)
        for num, count in counter.items():
            if count > (n//3):
                lst.append(num)
        return lst
        