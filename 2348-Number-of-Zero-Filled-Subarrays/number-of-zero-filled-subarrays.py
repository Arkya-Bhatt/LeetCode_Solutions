from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        result = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                combo = (zero_count * (zero_count+1))//2
                result += combo
                zero_count = 0
        combo = (zero_count * (zero_count+1))//2
        result += combo
        return result
        