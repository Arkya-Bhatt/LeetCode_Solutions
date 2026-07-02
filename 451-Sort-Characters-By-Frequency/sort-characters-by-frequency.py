class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(s)
        parts = sorted(cnt.items(), key = lambda x: x[1], reverse = True)
        return "".join(ch * freq for ch, freq in parts)
        