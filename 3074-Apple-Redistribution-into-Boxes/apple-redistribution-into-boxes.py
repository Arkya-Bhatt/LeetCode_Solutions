from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total = sum(apple)
        capacity.sort(reverse = True)
        count = 0
        curr = 0
        for c in capacity:
            curr += c
            count += 1
            if curr >= total:
                return count
        return count
        