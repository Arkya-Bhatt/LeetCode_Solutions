class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        nL = moves.count("L")
        nR = moves.count("R")
        empty_space = len(moves) - nL - nR
        return abs(nR - nL) + empty_space
        