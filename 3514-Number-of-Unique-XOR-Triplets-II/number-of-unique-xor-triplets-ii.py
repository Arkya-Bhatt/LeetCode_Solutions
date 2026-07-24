from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        pair_xors = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                pair_xors.add(nums[i] ^ nums[j])
        triplet_xors = set()
        for x in pair_xors:
            for y in nums:
                triplet_xors.add(x ^ y)
        return len(triplet_xors)
        