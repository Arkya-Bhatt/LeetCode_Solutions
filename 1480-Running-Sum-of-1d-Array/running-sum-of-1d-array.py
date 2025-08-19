from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prev_ele = prefix_sum[-1]
            curr_ele = nums[i]
            curr_sum = prev_ele + curr_ele
            prefix_sum.append(curr_sum)
        return prefix_sum