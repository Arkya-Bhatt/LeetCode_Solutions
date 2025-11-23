class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime_set = {2, 3, 5, 7, 11, 13, 17, 19}
        def count_set_bits(x: int) -> int:
            return bin(x).count('1')
        count = 0
        for num in range(left, right + 1):
            if count_set_bits(num) in prime_set:
                count += 1
        return count
        