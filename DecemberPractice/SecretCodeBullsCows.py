import os
import random

os.system("clear")

code = "".join(random.sample("0123456789", 4))
print(f"#SECRET CODE (for testing purposes): {code}")

attempts = 0
guesses_left = 9

guess = input(f"ENTER YOUR GUESS (4 UNIQUE DIGITS) ({guesses_left} guesses left): ")
while len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
    print("invalid input.")
    guess = input(f"ENTER YOUR GUESS (4 UNIQUE DIGITS) ({guesses_left} guesses left): ")
guesses_left -= 1

while guess != code:
    attempts += 1
    bulls = sum(1 for g in guess if g == code[guess.index(g)])
    cows = sum(1 for g in guess if g in code) - bulls
    print(f"Bulls: {bulls}\nCows: {cows}")
    print()

    guess = input(f"ENTER YOUR GUESS (4 UNIQUE DIGITS) ({guesses_left} guesses left): ")
    while len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
        print("invalid input.")
        guess = input(f"ENTER YOUR GUESS (4 UNIQUE DIGITS) ({guesses_left} guesses left): ")
    guesses_left -= 1

    if guesses_left == 0:
        print(f"you've run out of guesses. the secret code was {code}.")
        exit()
        

print("correct! you've guessed the secret code.")
print(f"it took you {attempts} attempts.")