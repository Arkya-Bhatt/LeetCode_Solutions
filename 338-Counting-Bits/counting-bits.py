from typing import List

class Solution:
    def countOne(self, n : int) -> int:
        x = str(n)
        count = 0
        for i in x:
            if i == "1":
                count += 1
        return count

    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            ans[i] = self.countOne(bin(i)[2:])
        return ans
        