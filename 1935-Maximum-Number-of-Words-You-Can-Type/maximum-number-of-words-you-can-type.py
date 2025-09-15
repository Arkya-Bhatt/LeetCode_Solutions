class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ")
        brokenLetters = set(brokenLetters)
        count = len(text)
        for word in text:
            if brokenLetters & set(word):
                count -= 1
        return count
