from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if not s or not t or m < n:
            return ""
        target_counts = defaultdict(int)
        for char in t:
            target_counts[char] += 1
        required = len(target_counts)
        left, right = 0, 0
        formed = 0
        window_counts = defaultdict(int)
        ans = float('inf'), None, None
        while right < len(s):
            char = s[right]
            window_counts[char] += 1
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
            while left <= right and formed == required:
                char_left = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window_counts[char_left] -= 1
                if char_left in target_counts and window_counts[char_left] < target_counts[char_left]:
                    formed -= 1
                left += 1
            right += 1
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]
        