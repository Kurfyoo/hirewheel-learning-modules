import os

os.system("clear")

try:
    weight = float(input("ENTER YOUR WEIGHT IN KILOGRAMS: "))
    height = float(input("ENTER YOUR HEIGHT IN METERS: "))
    bmi = weight / (height ** 2)
except:
    print("invalid input.")
    exit()

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {round(bmi, 2)} → Category: {category}")