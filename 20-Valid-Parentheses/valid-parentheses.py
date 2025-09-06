class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in brackets_map.values():
                stack.append(char)
            elif char in brackets_map.keys():
                if not stack or brackets_map[char] != stack.pop():
                    return False
        return not stack
