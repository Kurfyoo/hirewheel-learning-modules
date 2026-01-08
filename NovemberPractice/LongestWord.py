import os

os.system("clear")

phrase = input("ENTER A PHRASE OR SENTENCE: ")
words = phrase.split()
if len(words) == 0:
    print("no words found")
    exit()
longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print("The longest word is:", longest_word)