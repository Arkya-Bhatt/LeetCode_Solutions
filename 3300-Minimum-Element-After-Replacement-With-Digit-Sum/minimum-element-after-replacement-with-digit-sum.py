from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_value = float("inf")
        for n in nums:
            digit_sum = 0
            curr = n
            while curr > 0:
                digit_sum += curr % 10
                curr //= 10
            min_value = min(min_value, digit_sum)
        return min_value
        