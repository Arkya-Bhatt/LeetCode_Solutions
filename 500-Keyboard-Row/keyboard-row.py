from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]
        ans = []
        for word in words:
            s = set(word.lower())
            if any(s <= row for row in rows):
                ans.append(word)
        return ans
        