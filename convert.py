# Lab 1
# Group #5
# Authors: Kiyale Olden and Matheus Souza
# Date: 02/03/2024
# *** This program converts temperature between Fahrenheit and Celsius units ***

print("Welcome to the Olden-Souza Python Converter!")
print("Choose what you would like to:")
print("1. Distance Conversion (miles <-> kilometers)")
print("2. Currency Conversion (USD <-> Euro)")
print("3. Temperature Conversion: (Celsius <-> Fahrenheit)")

choice = input("Enter your choice (1, 2, or 3): ")

if choice == '1':
    print("*** Distance Conversion: miles <-> kilometers ***")
    conversion_type = input("Enter 1 for miles to kilometers, 2 for kilometers to miles: ")
    if conversion_type == '1':
        distance = float(input("Enter distance: "))
        converted_distance = distance * 1.60934
        print(f"{distance} miles = {converted_distance:.2f} kilometers")
    elif conversion_type == '2':
        distance = float(input("Enter distance: "))
        converted_distance = distance / 1.60934
        print(f"{distance} kilometers = {converted_distance:.2f} miles")
    else:
        print("Invalid choice for distance conversion.")

elif choice == '2':
    print("*** Currency Conversion: USD <-> Euro ***")
    amount_usd = float(input("Enter amount in USD: "))
    # Assuming a static exchange rate for demonstration purposes
    exchange_rate = 0.95  # 1 USD to Euro conversion rate
    converted_amount = amount_usd * exchange_rate
    print(f"USD {amount_usd} = EUR {converted_amount:.2f}")

elif choice == '3':
    print("*** Temperature Conversion: (Celsius <-> Fahrenheit) ***")
    conversion_type = input("Enter 1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius: ")
    if conversion_type == '1':
    # coverts celsius to fahrenheit
        temperature = int(input("Enter the temperature: "))
        converted_temperature = (temperature * 9/5) + 32
        print(f"{temperature:.2f}°C = {converted_temperature:.2f}°F")
    elif conversion_type == '2':
    # converts fahrenheit to celsius
        temperature = int(input("Enter the temperature: "))
        converted_temperature = (temperature - 32) * 5/9
        print(f"{temperature:.2f}°F = {converted_temperature:.2f}°C")

else:
    print("Invalid choice. Please restart and enter 1 or 2.")
