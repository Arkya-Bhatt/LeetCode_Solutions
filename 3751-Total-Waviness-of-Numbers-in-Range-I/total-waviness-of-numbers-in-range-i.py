from typing import List

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for n in range(num1, num2 + 1):
            s = str(n)
            if len(s) < 3:
                continue
            for i in range(1, len(s) - 1):
                if s[i] > s[i - 1] and s[i] > s[i + 1]:
                    ans += 1
                elif s[i] < s[i - 1] and s[i] < s[i + 1]:
                    ans += 1
        return ans
        