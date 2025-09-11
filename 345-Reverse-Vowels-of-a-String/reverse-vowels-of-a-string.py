class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        str_lst = list(s)
        start = 0
        end = len(str_lst) - 1
        while start < end:
            if str_lst[start] in vowels and str_lst[end] in vowels:
                temp = str_lst[start]
                str_lst[start] = str_lst[end]
                str_lst[end] = temp
                start += 1
                end -= 1
            elif str_lst[start] not in vowels:
                start += 1
            elif str_lst[end] not in vowels:
                end -= 1
        return "".join(str_lst)