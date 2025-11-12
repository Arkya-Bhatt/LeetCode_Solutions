from typing import List
from math import gcd

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones_count = nums.count(1)
        if ones_count > 0:
            return n - ones_count
        
        min_len = n + 1
        for i in range(n):
            cur_gcd = nums[i]
            for j in range(i + 1, n):
                cur_gcd = gcd(cur_gcd, nums[j])
                if cur_gcd == 1:
                    min_len = min(min_len, j - i + 1)
                    break
        
        if min_len > n:
            return -1
        return min_len - 1 + n - 1
        