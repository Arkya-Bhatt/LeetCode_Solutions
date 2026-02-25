from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bits(n: int) -> int:
            return bin(n)[2:].count("1")
        arr.sort(key = lambda x: (count_bits(x), x))
        return arr
        