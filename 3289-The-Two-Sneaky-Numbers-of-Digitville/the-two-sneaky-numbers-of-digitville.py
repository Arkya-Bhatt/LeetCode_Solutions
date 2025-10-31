from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        my_dict = Counter(nums)
        res = []
        for k, v in my_dict.items():
            if v == 2:
                res.append(k)
        return res
    