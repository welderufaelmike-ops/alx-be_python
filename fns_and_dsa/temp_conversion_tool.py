
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit:.1f}°F is {celsius}°C")

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius:.1f}°C is {fahrenheit:.1f}°F")

# Main program
try:
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        convert_to_celsius(temp)
    elif unit == "C":
        convert_to_fahrenheit(temp)
    else:
        print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    

# This code list option for users to pick and it interact with user.
AHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def display_temp():
    print("1. convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius:.2f}°C")
   
def convert_to_fahrenheit(celsius):
    fahrenheit =  (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {fahrenheit:.2f}°F")
    
display_temp()   
choice = input("choose an option (1 or 2): ")
if choice == "1":
    f=float(input("Enter temperature in fahrenheit: "))
    convert_to_celsius(f)
elif choice == "2":
    c = float(input("Enter temperature in Celsius: "))
    convert_to_fahrenheit(c)
else:
    print("invalid choice")
