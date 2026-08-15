class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import Counter
        cnt = Counter()
        l = 0
        ans = 0
        for r, ch in enumerate(s):
            cnt[ch] += 1
            while cnt[ch] > 2:
                cnt[s[l]] -= 1
                l += 1
            ans = max(ans, (r - l + 1))
        return ans
        