class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        for i, _ in enumerate(word):
            ans += i // 8 + 1
        return ans
        