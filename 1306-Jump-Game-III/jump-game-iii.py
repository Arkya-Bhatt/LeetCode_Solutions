from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import deque
        n = len(arr)
        q = deque([start])
        seen = [False] * n
        seen[start] = True
        while q:
            i = q.popleft()
            if arr[i] == 0:
                return True
            for nxt in [i + arr[i], i - arr[i]]:
                if 0 <= nxt < n and not seen[nxt]:
                    seen[nxt] = True
                    q.append(nxt)
        return False
        