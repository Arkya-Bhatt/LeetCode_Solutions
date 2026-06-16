class Solution:
    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c.islower():
                result.append(c)
            elif c == "*":
                if result:
                    result.pop()
            elif c == "#":
                result = result + result
            elif c == "%":
                result = result[::-1]
        return "".join(result)
        