from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        smallest, second_smallest = float('inf'), float('inf')
        for i in range(1, len(nums)):
            if nums[i] < smallest:
                second_smallest = smallest
                smallest = nums[i]
            elif nums[i] < second_smallest:
                second_smallest = nums[i]        
        return first + smallest + second_smallest
        