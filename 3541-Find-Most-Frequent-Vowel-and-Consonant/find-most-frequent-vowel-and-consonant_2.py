class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        max_vowel_freq = 0
        max_consonant_freq = 0
        hash_set = set(s)

        for char in hash_set:
            if char in vowels:
                max_vowel_freq = max(max_vowel_freq, s.count(char))
            else:
                max_consonant_freq = max(max_consonant_freq, s.count(char))

        return max_vowel_freq + max_consonant_freq
        