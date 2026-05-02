class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = [0] * (n + 1)
        count = 0
        for i in range(1, n + 1):
            tens = dp[i // 10]
            ones = i % 10
            if ones in (3, 4, 7):
                dp[i] = 0
            elif tens == 0 and i >= 10:
                dp[i] = 0
            elif tens <= 1 and ones in (0, 1, 8):
                dp[i] = 1
            else:
                dp[i] = 2
                count += 1
        return count
        