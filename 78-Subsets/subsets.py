from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper_func(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                helper_func(i + 1, path)
                path.pop()
        helper_func(0, [])
        return res
        