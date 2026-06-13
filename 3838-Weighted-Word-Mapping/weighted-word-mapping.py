from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result = []
        for word in words:
            total_weight = 0
            for char in word:
                index = ord(char) - ord('a')
                total_weight += weights[index]
            mapped_char = chr(ord('z') - (total_weight % 26))
            result.append(mapped_char)
        return ''.join(result)
        