from typing import List

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n = len(dimensions)
        max_diag_len = -1
        max_area = -1
        for i in range(n):
            l = dimensions[i][0]
            b = dimensions[i][1]
            curr_diag_len = (l**2 + b**2)**(1/2)
            curr_area = l*b
            if curr_diag_len > max_diag_len:
                max_diag_len = curr_diag_len
                max_area = curr_area
            elif curr_diag_len == max_diag_len:
                if curr_area > max_area:
                    max_area = curr_area
        return max_area
        