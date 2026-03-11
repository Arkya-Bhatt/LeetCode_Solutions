class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 0
        else:
            n_bin = bin(n)[2:]
            n_bin_list = list(n_bin)
            for i in range(len(n_bin_list)):
                if n_bin_list[i] == "0":
                    n_bin_list[i] = "1"
                else:
                    n_bin_list[i] = "0"
            return int("".join(n_bin_list), 2)
        