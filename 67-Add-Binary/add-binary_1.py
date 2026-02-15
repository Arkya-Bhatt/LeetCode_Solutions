class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p = int(a,2)
        q = int(b,2)
        res = bin(p+q)[2:]
        return res