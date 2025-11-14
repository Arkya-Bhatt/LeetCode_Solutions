from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()
        for left in range(len(s)-9):
            curr = s[left : left+10]
            if curr in seen:
                res.add(curr)
            seen.add(curr)
        return list(res)
