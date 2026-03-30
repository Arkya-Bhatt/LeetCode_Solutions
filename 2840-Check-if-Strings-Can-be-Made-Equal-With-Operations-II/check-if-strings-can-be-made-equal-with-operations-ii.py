class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        count = [[0] * 26 for _ in range(2)]
        for i in range(len(s1)):
            count[i % 2][ord(s1[i]) - ord('a')] += 1
            count[i % 2][ord(s2[i]) - ord('a')] -= 1
        for i in range(26):
            if count[0][i] != 0 or count[1][i] != 0:
                return False
        return True
        