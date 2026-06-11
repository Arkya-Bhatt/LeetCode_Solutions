from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        mod = 10**9 + 7
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        max_depth = 0
        queue = deque([(1, 0, -1)])
        while queue:
            node, level, parent = queue.popleft()
            max_depth = max(max_depth, level)
            for neighbor in adj[node]:
                if neighbor != parent:
                    queue.append((neighbor, level + 1, node))
        return pow(2, max_depth - 1, mod)
        