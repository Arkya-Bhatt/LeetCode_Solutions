from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        start = 0
        end = n-1
        while start < end:
            curr_sum = numbers[start] + numbers[end]
            if curr_sum == target:
                return [(start+1), (end+1)]
            if curr_sum < target:
                start += 1
            if curr_sum > target:
                end -= 1
        return []
        