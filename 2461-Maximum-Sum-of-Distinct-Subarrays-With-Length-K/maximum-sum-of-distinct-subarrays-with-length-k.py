from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        elements = set()
        current_sum = 0
        max_sum = 0
        left = 0

        for right in range(n): 
            if nums[right] not in elements:
                current_sum += nums[right]
                elements.add(nums[right])

                if right - left + 1 == k:
                    if current_sum > max_sum:
                        max_sum = current_sum
                    
                    current_sum -= nums[left]
                    elements.remove(nums[left])
                    left += 1
            else:
                while nums[left] != nums[right]:
                    current_sum -= nums[left]
                    elements.remove(nums[left])
                    left += 1
                
                left += 1

        return max_sum
        