from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        
        def check(side: int) -> bool:
            for i in range(side, m + 1):
                for j in range(side, n + 1):
                    total = (prefix[i][j] - prefix[i-side][j] - prefix[i][j-side] + prefix[i-side][j-side])
                    if total <= threshold:
                        return True
            return False
            
        left, right = 0, min(m, n)
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        return left if check(left) else 0
