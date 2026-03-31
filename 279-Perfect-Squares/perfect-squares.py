from math import inf

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [inf] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            i = 1
            while i * i <= j:
                dp[j] = min(dp[j], dp[j - i * i] + 1)
                i += 1
        return dp[n]
        