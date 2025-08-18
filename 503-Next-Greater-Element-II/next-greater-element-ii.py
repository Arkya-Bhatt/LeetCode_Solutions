from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n
        for i in range(2*n):
            curr_idx = i % n
            while stack and nums[curr_idx] > nums[stack[-1]]:
                popped_idx = stack.pop()
                ans[popped_idx] = nums[curr_idx]
            stack.append(curr_idx)
        return ans
        