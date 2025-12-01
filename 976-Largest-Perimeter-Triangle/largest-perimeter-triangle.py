from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def valid_triangle(a, b, c):
            if (a + b > c) and (b + c > a) and (c + a > b):
                return True
            return False
        max_perimeter = 0
        nums.sort(reverse = True)
        n = len(nums)
        for i in range(n - 2):
            if valid_triangle(nums[i], nums[i + 1], nums[i + 2]):
                max_perimeter = max(max_perimeter, nums[i] + nums[i + 1] + nums[i + 2])
        return max_perimeter
        