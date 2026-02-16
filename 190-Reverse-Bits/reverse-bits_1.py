class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = bin(n)[2:].zfill(32)
        bin_res = bin_n[::-1]
        res = int(bin_res, 2)
        return res
        