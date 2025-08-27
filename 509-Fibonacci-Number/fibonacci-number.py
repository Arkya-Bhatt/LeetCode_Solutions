class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dic = {}
        dic[0], dic[1] = 0, 1
        for i in range(2, n+1):
            dic[i] = dic[i-1] + dic[i-2]
        return dic[n]
        