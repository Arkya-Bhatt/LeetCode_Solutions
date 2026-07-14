class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        count = [0] * 26
        curr = 0
        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(ch) == 25):
                curr += 1
            else:
                curr = 1
            idx = ord(ch) - ord("a")
            count[idx] = max(count[idx], curr)
        return sum(count)
        