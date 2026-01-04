import math
import os

os.system("clear")

# rounds down to three digits
def truncate(num):
    return math.trunc(num*1000)/1000

shape = input("ENTER SHAPE: ").lower()

try:
    if shape == "circle":
        radius = float(input("ENTER RADIUS: "))
        print("Area: "+str(truncate(math.pi*(radius**2))))

    elif shape == "triangle":
        base = float(input("ENTER BASE: "))
        height = float(input("ENTER HEIGHT: "))
        print("Area: "+str(truncate(.5*base*height)))

    elif shape == "square" or shape == "rectangle":
        length = float(input("ENTER LENGTH: "))
        width = float(input("ENTER WIDTH: "))
        print("Area: "+str(truncate(length*width)))

    else:
        print("SHAPE UNAVAILABLE")

except ValueError:
    print("NaN")