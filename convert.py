# Lab 1
# Group #5
# Authors: Kiyale Olden and Matheus Souza
# Date: 02/03/2024
# *** This program converts temperature between Fahrenheit and Celsius units ***


print("*** Temperature Conversion: Celsius <-> Fahrenheit ***")

# prompt to select c to f or f to c
temperature = float(input("Enter temperature: "))
conversion_type = input("Enter 1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius: ")

if conversion_type == '1':
    # coverts celsius to fahrenheit
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature:.2f}°C = {converted_temperature:.2f}°F")
elif conversion_type == '2':
    # converts fahrenheit to celsius
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature:.2f}°F = {converted_temperature:.2f}°C")
else:
    print("Invalid choice. Please restart and enter 1 or 2.")
