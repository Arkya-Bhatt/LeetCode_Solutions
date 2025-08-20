class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        max_vowel_freq = 0
        for char in freq:
            if char in vowels:
                max_vowel_freq = max(max_vowel_freq, freq[char])
        
        max_consonant_freq = 0
        for char in freq:
            if char not in vowels:
                max_consonant_freq = max(max_consonant_freq, freq[char])

        return max_vowel_freq + max_consonant_freq
        