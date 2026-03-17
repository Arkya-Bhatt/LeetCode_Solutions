from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        ans = 0
        for i in range(m):
            matrix[i].sort(reverse=True)
            for j, h in enumerate(matrix[i]):
                ans = max(ans, (j + 1) * h)
        return ans
        