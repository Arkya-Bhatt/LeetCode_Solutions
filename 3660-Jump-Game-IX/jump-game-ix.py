from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prefix_max = [nums[0]] * n
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        suffix_min = float('inf')
        for i in range(n-1, -1, -1):
            if i + 1 < n:
                ans[i] = ans[i+1] if prefix_max[i] > suffix_min else prefix_max[i]
            else:
                ans[i] = prefix_max[i]
            suffix_min = min(suffix_min, nums[i])
        return ans
        