class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for ch in set(s):
            l, r = s.find(ch), s.rfind(ch)
            if r - l > 1:
                res += len(set(s[l+1:r]))
        return res
        