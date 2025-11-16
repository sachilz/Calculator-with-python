number1 = float(input("Enter first number : "))
number2 = float(input("Enter second number : "))

print("Select operaions : ")
print("1.  Addition")
print("2.  Subtraction")
print("3.  Multiplication")
print("4.  Division")

choice = input("Enter your choice (1/2/3/4) : ")

if choice == "1":
    print("Result : ", number1 + number2)

elif choice == "2":
    print("Result : ", number1 - number2)

elif choice == "3":
    print("Result : ", number1 * number2)

elif choice == "4":
    if number2 != 0:
        print("Result : ", number1 / number2)
    else:
        print("Error! can't perform Division by zero.")
