class Solution:
    def countCollisions(self, directions: str) -> int:
        s = directions.lstrip('L').rstrip('R')
        return sum(1 for c in s if c != 'S')
        