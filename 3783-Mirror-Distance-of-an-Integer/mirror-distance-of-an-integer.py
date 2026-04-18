class Solution:
    def reverse_integer(self, x: int) -> int:
        rev = 0
        while x != 0:
            d = x % 10
            rev = (rev * 10) + d
            x //= 10
        return rev
    def mirrorDistance(self, n: int) -> int:
        rev_int = self.reverse_integer(n)
        return abs(n - rev_int)
        