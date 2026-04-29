from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        a %= MOD
        
        def mod_pow(base: int, exp: int) -> int:
            result = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return result
        
        res = 1
        for digit in b:
            res = (mod_pow(res, 10) * mod_pow(a, digit)) % MOD
        
        return res
        