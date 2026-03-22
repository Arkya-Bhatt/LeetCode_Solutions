from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_90_clockwise(matrix: List[List[int]]) -> None:
            n = len(matrix)
            for l in range(n // 2):
                first, last = l, n - 1 - l
                for i in range(first, last):
                    offset = i - first
                    temp = matrix[first][i]
                    matrix[first][i] = matrix[last - offset][first]
                    matrix[last - offset][first] = matrix[last][last - offset]
                    matrix[last][last - offset] = matrix[i][last]
                    matrix[i][last] = temp
        
        if mat == target:
            return True
        for _ in range(3):
            rotate_90_clockwise(mat)
            if mat == target:
                return True
        return False
        