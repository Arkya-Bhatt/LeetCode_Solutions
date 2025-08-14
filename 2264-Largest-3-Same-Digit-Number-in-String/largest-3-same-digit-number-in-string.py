class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        max_good = ""
        for i in range(n-2):
            sub_str = num[i:i+3]
            if sub_str[0] == sub_str[1] == sub_str[2]:
                if max_good == "" or sub_str > max_good:
                    max_good = sub_str
        return max_good