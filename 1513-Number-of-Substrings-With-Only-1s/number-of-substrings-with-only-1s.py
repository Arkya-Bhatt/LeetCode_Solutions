class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        total = 0
        for c in s:
            if c == '1':
                count += 1
            else:
                total += count * (count + 1) // 2
                count = 0
        total += count * (count + 1) // 2
        return total % MOD
        