from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0
        n = len(nums)
        mp = {0: -1}
        cur = 0
        ans = n
        for i in range(n):
            cur = (cur + nums[i]) % p
            target = (cur - r) % p
            if target in mp:
                ans = min(ans, i - mp[target])
            mp[cur] = i
        return ans if ans < n else -1