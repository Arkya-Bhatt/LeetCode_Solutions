from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_values = sorted(set(arr))
        value_to_rank = {}
        current_rank = 1
        for value in unique_values:
            value_to_rank[value] = current_rank
            current_rank += 1
        result = []
        for num in arr:
            result.append(value_to_rank[num])
        return result
        