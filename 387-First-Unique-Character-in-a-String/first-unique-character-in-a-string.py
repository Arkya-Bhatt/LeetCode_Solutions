from typing import List
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1
        for idx, char in enumerate(s):
            if freq_map[char] == 1:
                return idx
        return -1
        