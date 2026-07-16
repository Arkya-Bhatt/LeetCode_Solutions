class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        import math
        prefix_gcd = []
        max_val = -1
        for num in nums:
            max_val = max(max_val, num)
            prefix_gcd.append(math.gcd(num, max_val))
        prefix_gcd.sort()
        ans = 0
        left, right = 0, len(prefix_gcd) - 1
        while left < right:
            ans += math.gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1
        return ans
        