import os
import sys
import time

def clear():
    os.system('clear')

def wait(clr=True):
    print()
    key = input("PRESS ENTER TO CONTINUE: ")
    while key != "":
        print("INVALID KEY")
        key = input("PRESS ENTER TO CONTINUE: ")
    if clr:
        clear()

def exit():
    print("Exiting the program.")
    sys.exit()

def pause(seconds):
    time.sleep(seconds)
