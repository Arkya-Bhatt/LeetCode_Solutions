class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import defaultdict

        count = defaultdict(int)
        for char in s:
            count[char] += 1

        stack = []
        visited = set()

        for char in s:
            count[char] -= 1

            if char in visited:
                continue

            while stack and char < stack[-1] and count[stack[-1]] > 0:
                removed_char = stack.pop()
                visited.remove(removed_char)

            stack.append(char)
            visited.add(char)

        return ''.join(stack)
        