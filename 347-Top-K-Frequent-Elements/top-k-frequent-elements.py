from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(len(buckets) - 1, 0, -1):
            if buckets[freq]:
                result.extend(buckets[freq])
                if len(result) >= k:
                    return result[:k]
        return result
        