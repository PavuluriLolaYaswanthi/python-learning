def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("1. KM to Miles")
print("2. Celsius to Fahrenheit")

choice = int(input("Choose option: "))

if choice == 1:
    km = float(input("Enter KM: "))
    print("Miles:", km_to_miles(km))

elif choice == 2:
    celsius = float(input("Enter Celsius: "))
    print("Fahrenheit:", celsius_to_fahrenheit(celsius))

else:
    print("Invalid choice")