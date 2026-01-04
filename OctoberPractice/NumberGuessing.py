import random

num = random.randint(1,100)

running = True

while running:
    try:
        guess = int(input("ENTER NUM (1-100): "))
        while guess != num: 
            if guess > num:
                print("Too high!")
                guess = int(input("ENTER NUM (1-100): "))
            
            if guess < num:
                print("Too low!")
                guess = int(input("ENTER NUM (1-100): "))
        
        running = False
    # catches non-numbers
    except ValueError:
        print("INVALID GUESS")

print("YOU GUESSED THE NUMBER!!!")