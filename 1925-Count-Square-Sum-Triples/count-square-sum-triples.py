class Solution:
    def countTriples(self, n: int) -> int:
        squares = {c * c for c in range(1, n + 1)}
        ans = 0
        for a in range(1, n + 1):
            a2 = a ** 2
            for b in range(1, n + 1):
                b2 = b ** 2
                if (a2 + b2) in squares:
                    ans += 1
        return ans
        