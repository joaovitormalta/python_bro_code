# Exercise 7: Calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = None

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = None

if result is not None:
    print(f"The result is: {result}")
else:
    print("Invalid operator.")