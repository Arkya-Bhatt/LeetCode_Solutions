from typing import List
import math

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) >= 2:
                a = stack[-2]
                b = stack[-1]
                g = math.gcd(a, b)
                if g > 1:
                    lcm = a * b // g
                    stack.pop()
                    stack.pop()
                    stack.append(lcm)
                else:
                    break
        return stack
        