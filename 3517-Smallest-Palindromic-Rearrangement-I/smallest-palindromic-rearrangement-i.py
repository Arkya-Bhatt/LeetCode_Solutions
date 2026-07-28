class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        left = sorted(s[:n // 2])
        mid = s[n // 2] if n % 2 else ""
        return "".join(left + [mid] + left[::-1])
        