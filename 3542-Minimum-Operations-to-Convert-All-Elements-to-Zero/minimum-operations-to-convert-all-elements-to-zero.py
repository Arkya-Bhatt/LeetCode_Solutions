from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        stack = [0]
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            if not stack or stack[-1] < num:
                ops += 1
                stack.append(num)
        return ops
        