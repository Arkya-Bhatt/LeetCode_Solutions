from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        cut = [False] * (n - 1)
        ans = 0
        for c in range(m):
            bad = False
            for i in range(n - 1):
                if not cut[i] and strs[i][c] > strs[i + 1][c]:
                    bad = True
                    break
            if bad:
                ans += 1
                continue
            for i in range(n - 1):
                if not cut[i] and strs[i][c] < strs[i + 1][c]:
                    cut[i] = True
        return ans
        