import os
import random

os.system("clear")

user_choice = input("ENTER ROCK, PAPER, OR SCISSORS: ").lower()

computer_choice = random.choice(["rock", "paper", "scissors"])
  
if user_choice not in ["rock", "paper", "scissors"]:
    print("invalid choice")
    exit()

print(f"The computer chose {computer_choice}.")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")