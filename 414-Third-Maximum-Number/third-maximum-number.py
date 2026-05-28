from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        lst = list(set(nums))
        lst.sort(reverse=True)
        if len(lst) >= 3:
            return lst[2]
        else:
            return lst[0]
        