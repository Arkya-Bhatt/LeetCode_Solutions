class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        length = 0
        odd_found = False
        for count in freq.values():
            pairs = count // 2
            length += pairs * 2
            if count % 2 != 0:
                odd_found = True
        if odd_found:
            length += 1
        return length
        