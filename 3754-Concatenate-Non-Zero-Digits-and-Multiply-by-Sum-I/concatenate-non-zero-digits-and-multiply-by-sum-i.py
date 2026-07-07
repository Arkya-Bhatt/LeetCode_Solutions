class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        p = 1
        s = 0
        while n > 0:
            d = n % 10
            if d != 0:
                x += d * p
                p *= 10
                s += d
            n //= 10
        return (x * s)
        