from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        max_len = 0
        for k in freq:
            if k+1 in freq:
                curr_len = freq[k] + freq[k+1]
                if curr_len > max_len:
                    max_len = curr_len
        return max_len