from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = n
        for i in range(n):
            if words[(startIndex + i) % n] == target:
                ans = min(ans, i)
            if words[(startIndex - i + n) % n] == target:
                ans = min(ans, i)
        return ans if ans < n else -1
        