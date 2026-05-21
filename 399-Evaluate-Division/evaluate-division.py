from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph = defaultdict(dict)

        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(src, dst, seen):
            if src == dst:
                return 1.0
            seen.add(src)
            for nei, weight in graph[src].items():
                if nei in seen:
                    continue
                res = dfs(nei, dst, seen)
                if res != -1.0:
                    return weight * res
            return -1.0

        ans = []
        for a, b in queries:
            if a not in graph or b not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(a, b, set()))
        return ans
