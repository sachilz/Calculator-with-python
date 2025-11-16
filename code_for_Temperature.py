print("temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose conversion (1/2): ")

if choice == '1':
    x = float(input("Enter temperature in Celsius: "))
    y = (x * 9/5) + 32
    print("Temperature in Fahrenheit:", round(y,2))

elif choice == '2':
    x = float(input("Enter temperature in Fahrenheit: "))
    y = (x - 32) * 5/9
    print("Temperature in Celsius:", round(y,2))