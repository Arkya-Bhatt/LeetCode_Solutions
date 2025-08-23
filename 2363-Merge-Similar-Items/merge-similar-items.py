from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        weight_map = {}

        for v, w in items1:
            if v in weight_map:
                weight_map[v] += w
            else:
                weight_map[v] = w
                
        for v, w in items2:
            if v in weight_map:
                weight_map[v] += w
            else:
                weight_map[v] = w
        
        ret = []
        for val, wt in weight_map.items():
            ret.append([val, wt])

        ret.sort(key = lambda x: x[0])
        return ret
