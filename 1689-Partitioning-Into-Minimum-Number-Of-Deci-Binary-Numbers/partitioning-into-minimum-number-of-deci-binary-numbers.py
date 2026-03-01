class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = 0
        for char in n:
            max_digit = max(max_digit, int(char))
        return max_digit
        