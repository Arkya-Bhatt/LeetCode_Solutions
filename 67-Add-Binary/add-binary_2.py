class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            summ = carry
            if i >= 0:
                summ += int(a[i])
            if j >= 0:
                summ += int(b[j])
            result.append(str(summ % 2))
            carry = summ // 2
            i -= 1
            j -= 1
        return "".join(result[::-1])
        