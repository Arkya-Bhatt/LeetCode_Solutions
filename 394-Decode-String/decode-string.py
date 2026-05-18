class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        res = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((res, num))
                res = ""
                num = 0
            elif ch == "]":
                prev_res, k = stack.pop()
                res = prev_res + k * res
            else:
                res += ch
        return res
        