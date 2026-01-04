phrase = input("ENTER A PHRASE OR SENTENCE: ")
phrase = "".join(ltr for ltr in phrase if ltr.isalpha() or ltr == " ")
acronym = "".join(word[0].upper() for word in phrase.split())
print(acronym)