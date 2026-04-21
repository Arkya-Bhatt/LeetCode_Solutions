class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        total = 10
        cur = 9
        for k in range(2, min(n, 10) + 1):
            cur = cur * (10 - k + 1)
            total += cur
        return total
        