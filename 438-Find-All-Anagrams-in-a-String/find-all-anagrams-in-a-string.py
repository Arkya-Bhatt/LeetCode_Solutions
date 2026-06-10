from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        res = []
        len_p = len(p)
        cnt_p = Counter(p)
        cnt_s = Counter(s[:len_p - 1])
        for i in range(len_p - 1, len(s)):
            cnt_s[s[i]] += 1
            if cnt_s == cnt_p:
                res.append(i - len_p + 1)
            cnt_s[s[i - len_p + 1]] -= 1
            if cnt_s[s[i - len_p + 1]] == 0:
                del cnt_s[s[i - len_p + 1]]
        return res
        