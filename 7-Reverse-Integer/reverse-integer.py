class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if x < 0:
            s = s[1:]
            reversed_s = s[::-1]
            reversed_s = '-' + reversed_s
        else:
            reversed_s = s[::-1]
        reversed_x = int(reversed_s)
        if (reversed_x < (-2**31)) or (reversed_x > (2**31 - 1)):
            return 0
        return reversed_x
        