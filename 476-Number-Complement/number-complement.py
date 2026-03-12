class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        elif num == 1:
            return 0
        else:
            num_bin = bin(num)[2:]
            num_bin_list = list(num_bin)
            for i in range(len(num_bin_list)):
                if num_bin_list[i] == "0":
                    num_bin_list[i] = "1"
                else:
                    num_bin_list[i] = "0"
            return int("".join(num_bin_list), 2)
        