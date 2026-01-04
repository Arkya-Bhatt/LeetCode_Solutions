from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            div_sum = 0
            count = 0
            i = 1
            while i * i <= n:
                if n % i == 0:
                    j = n // i
                    if i == j:
                        count += 1
                        div_sum += i
                    else:
                        count += 2
                        div_sum += i + j
                    if count > 4:
                        break
                i += 1
            if count == 4:
                total += div_sum
        return total
        