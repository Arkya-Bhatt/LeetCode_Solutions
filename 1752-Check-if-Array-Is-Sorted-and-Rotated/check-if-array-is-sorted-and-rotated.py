from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        count_drop = 0
        for i in range(len(nums)-1):
            if (nums[i] > nums[i+1]):
                count_drop += 1
        if (nums[-1] > nums[0]):
            count_drop += 1
        if count_drop > 1:
            return False
        return True