from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            prefix_sum += nums[i]
        present = set(nums)
        answer = prefix_sum
        while answer in present:
            answer += 1
        return answer
        