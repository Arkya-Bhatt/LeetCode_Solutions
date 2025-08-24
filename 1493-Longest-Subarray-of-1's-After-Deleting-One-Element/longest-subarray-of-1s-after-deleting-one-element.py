from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        zeros = 0
        max_ones = 0
        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            length = right - left + 1
            ones = length - zeros
            if ones > max_ones:
                max_ones = ones
        if max_ones == n:
            return n-1
        return max_ones
        