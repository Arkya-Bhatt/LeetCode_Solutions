class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        op = 0
        a, b = num1, num2
        while a and b:
            if a >= b:
                op += a // b
                a %= b
            else:
                op += b // a
                b %= a
        return op
        