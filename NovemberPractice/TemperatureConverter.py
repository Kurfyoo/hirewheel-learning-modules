import os

os.system("clear")

try:
    init_unit = input("INITIAL TEMPERATURE UNIT: ").lower()
    final_unit = input("FINAL TEMPERATURE UNIT: ").lower()
    init_temp = float(input("TEMPERATURE IN DEGREES: "))
except:
    print("invalid input")
    os.system("exit")

if not(final_unit in ["celsius", "fahrenheit", "kelvin"] and init_unit in ["celsius", "fahrenheit", "kelvin"]):
    print("invalid units")
    os.system("exit")

if final_unit == init_unit:
    print("same units")
    os.system("exit")

if init_unit == "celsius":
    if final_unit == "fahrenheit":
        final_temp = (init_temp * 9/5) + 32
        print(f"{init_temp}° Celsius is {final_temp}° Fahrenheit.")
    if final_unit == "kelvin":
        final_temp = init_temp + 273.15
        print(f"{init_temp}° Celsius is {final_temp}° Kelvin.")
elif init_unit == "fahrenheit":
    if final_unit == "celsius":
        final_temp = (init_temp - 32) * 5/9
        print(f"{init_temp}° Fahrenheit is {final_temp}° Celsius.")
    if final_unit == "kelvin":
        final_temp = (init_temp + 459.67) * 5/9
        print(f"{init_temp}° Fahrenheit is {final_temp}° Kelvin.")
elif init_unit == "kelvin":
    if final_unit == "celsius":
        final_temp = init_temp - 273.15
        print(f"{init_temp}° Kelvin is {final_temp}° Celsius.")
    if final_unit == "fahrenheit":
        final_temp = (init_temp * 9/5) - 459.67
        print(f"{init_temp}° Kelvin is {final_temp}° Fahrenheit.")