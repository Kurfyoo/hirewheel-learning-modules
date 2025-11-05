# imports
import os

# functions
def onlyAlpha(str):
    worde = ""
    for i in str:
        if i.isalpha:
            worde += i
    return worde

# main code
os.system('clear')

## cleaning up the word so that is is ONLY lowercase alphabetic chars.
word = (input("Enter a word: ")).lower()
word = onlyAlpha(word)
print(word)

## checking if the reverse of the word is the same as the word.
drow = word[::-1]
if drow == word:
    print("This word is a palindrome.")
else:
    print("This word is NOT a palindrome.")