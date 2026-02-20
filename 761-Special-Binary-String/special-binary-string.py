class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count = 0
        start = 0
        specials = []
        for i, char in enumerate(s):
            if char == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                inner = s[start+1:i]
                specials.append("1" + self.makeLargestSpecial(inner) + "0")
                start = i + 1
        specials.sort(reverse=True)
        return "".join(specials)
        