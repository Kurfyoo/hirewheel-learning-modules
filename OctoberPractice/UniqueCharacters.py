import os

os.system("clear")

word = input("ENTER WORD: ")

only_unique = True
for i in word:
    if word.count(i) > 1:
        only_unique = False
        break
    word.replace(i, "")

if word == "":
    print("The word is empty.")
elif only_unique:
    print("The word contains only unique characters.")
else:
    print("The word contains repeats of characters.")