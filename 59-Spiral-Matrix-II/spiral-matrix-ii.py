from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for x in range(n)]
        i = 0
        left, top, right, bottom = 0, 0, n, n
        while (left < right and top < bottom):
            for c in range(left, right):
                i += 1
                ans[left][c] = i
            top += 1
            for r in range(top, bottom):
                i += 1
                ans[r][right-1] = i
            right -= 1
            for c in range(right - 1, left - 1, -1):
                i += 1
                ans[bottom-1][c] = i
            bottom -= 1
            for r in range(bottom - 1, top - 1, -1):
                i += 1
                ans[r][left] = i
            left += 1
        return ans
        