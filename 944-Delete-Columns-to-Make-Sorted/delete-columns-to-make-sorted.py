from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        ans = 0
        for col_idx in range(cols):
            for row_idx in range(1, rows):
                if strs[row_idx][col_idx] < strs[row_idx - 1][col_idx]:
                    ans += 1
                    break
        return ans
        