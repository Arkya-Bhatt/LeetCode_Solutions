class Solution:
    def findNthDigit(self, n: int) -> int:
        k = 1
        cnt = 9
        while k * cnt < n:
            n -= k * cnt
            k += 1
            cnt *= 10
        start = 10 ** (k - 1)
        num = start + (n - 1) // k
        idx = (n - 1) % k
        return int(str(num)[idx])
        