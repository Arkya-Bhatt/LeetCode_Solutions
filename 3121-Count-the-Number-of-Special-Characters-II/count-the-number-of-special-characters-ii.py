class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        from collections import defaultdict
        import string

        lower = defaultdict(bool)
        upper = defaultdict(bool)
        for c in word:
            if c.islower():
                lower[c] = not upper[c.upper()]
            else:
                upper[c] = True
        return sum(lower[a] and upper[b] for a, b in zip(string.ascii_lowercase, string.ascii_uppercase))
        