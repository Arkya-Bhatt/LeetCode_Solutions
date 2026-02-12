class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for i in range(n):
            freq = [0] * 26
            distinct = 0
            max_freq = 0
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1
                max_freq = max(max_freq, freq[idx])
                if (j - i + 1) == distinct * max_freq:
                    max_len = max(max_len, j - i + 1)
        return max_len
        