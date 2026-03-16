class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    temp = stack.pop()
                    if temp // num < 0 and temp % num != 0:
                        stack.append(temp // num + 1)
                    else:
                        stack.append(temp // num)
                sign = s[i]
                num = 0
        return sum(stack)
        