print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print("Temperature in Fahrenheit:", round(f, 2))

elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Temperature in Celsius:", round(c, 2))

else:
    print("Invalid choice!")
