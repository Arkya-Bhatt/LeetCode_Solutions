from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = {}
        for dmg in power:
            count[dmg] = count.get(dmg, 0) + 1
        unique = sorted(count.keys())
        dp = [0] * (len(unique)+1)
        for i in range(len(unique)):
            total = unique[i] * count[unique[i]]
            j = i+1
            while j < len(unique) and abs(unique[j] - unique[i]) <= 2:
                j += 1
            dp[j] = max(dp[j], dp[i] + total)
            dp[i+1] = max(dp[i+1], dp[i])
        return max(dp)
        