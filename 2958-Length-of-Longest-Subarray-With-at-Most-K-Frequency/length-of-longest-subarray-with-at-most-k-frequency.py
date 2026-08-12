from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        left = 0
        max_len = 0
        for right, val in enumerate(nums):
            freq[val] += 1
            while freq[val] > k:
                freq[nums[left]] -= 1
                left += 1
            max_len = max(max_len, (right - left + 1))
        return max_len
        