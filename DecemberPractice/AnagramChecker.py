import os

from collections import Counter

os.system("clear")

word1 = input("ENTER THE FIRST WORD: ").lower()

word1 = "".join(ltr for ltr in word1 if ltr.isalpha())

word2 = input("ENTER THE SECOND WORD: ").lower()

word2 = "".join(ltr for ltr in word2 if ltr.isalpha())

if Counter(word1) == Counter(word2):
    print(f'"{word1}" and "{word2}" are anagrams.')
else:
    print(f'"{word1}" and "{word2}" are not anagrams.')