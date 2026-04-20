from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        left = 0
        while left < n and colors[left] == colors[-1]:
            left += 1
         
        right = n - 1
        while right >= 0 and colors[right] == colors[0]:
            right -= 1
        
        return max(n - 1 - left, right - 0)
        