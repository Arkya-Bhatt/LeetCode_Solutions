class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        res = ""
        for _ in range(8):
            res = hex_chars[num & 15] + res
            num >>= 4
            if num == 0:
                break
        return res.lstrip("0") or "0"
        