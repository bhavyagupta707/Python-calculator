import math

print("=== Simple Calculator ===")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Power (^)")
print("6. Percentage (%)")
print("7. Square Root (√)")

choice = input("Enter your choice (1-7): ")

if choice == "1":
    print("Result =", num1 + num2)

elif choice == "2":
    print("Result =", num1 - num2)

elif choice == "3":
    print("Result =", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")

elif choice == "5":
    print("Result =", num1 ** num2)

elif choice == "6":
    print("Result =", (num1 / 100) * num2)

elif choice == "7":
    print("Square Root of", num1, "=", math.sqrt(num1))

else:
    print("Invalid Choice")