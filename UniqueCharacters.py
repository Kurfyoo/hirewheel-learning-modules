import toolbox as tb

tb.clear()

word = input("ENTER WORD: ")

only_unique = True
for idx, ltr in enumerate(word):
    if word.count(ltr) > 1:
        only_unique = False
    word.replace(ltr, "")

if only_unique:
    print("The word contains only unique characters.")
else:
    print("The word contains repeats of characters.")