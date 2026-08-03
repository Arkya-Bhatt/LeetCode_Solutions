from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        from math import sqrt
        width = int(sqrt(area))
        while area % width != 0:
            width -= 1
        length = area // width
        return [length, width]
        