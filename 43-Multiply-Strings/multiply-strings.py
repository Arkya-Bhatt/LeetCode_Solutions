class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                total = mul + res[i + j + 1]
                res[i + j + 1] = total % 10
                res[i + j] += total // 10
        result_str = []
        for num in res:
            if not result_str and num == 0:
                continue
            result_str.append(str(num))
        return ''.join(result_str)
        