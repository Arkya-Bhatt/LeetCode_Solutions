class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)
        count = 0
        for i in range(26):
            lower = chr(ord("a") + i)
            upper = chr(ord("A") + i)
            if lower in chars and upper in chars:
                count += 1
        return count
        