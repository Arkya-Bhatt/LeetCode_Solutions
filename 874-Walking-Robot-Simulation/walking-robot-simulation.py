from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs_set = set((o[0], o[1]) for o in obstacles)
        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        x, y, d = 0, 0, 0
        max_dist = 0
        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d + 3) % 4
            else:
                for _ in range(cmd):
                    nx, ny = x + dx[d], y + dy[d]
                    if (nx, ny) in obs_set:
                        break
                    x, y = nx, ny
                    max_dist = max(max_dist, x*x + y*y)
        return max_dist
        