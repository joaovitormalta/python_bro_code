# name = input("Enter your name: ")

# while name == "":
#     print("You didn't enter your name.")
#     name = input("Enter your name: ")
# print(f"Hello, {name}!")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age cannot be negative.")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old.")

# food = input("Enter a food you like (q to quit): ")

# while food != "q":
#     print(f"You like {food}.")
#     food = input("Enter a food you like (q to quit): ")

# print("Thank you for sharing your food preferences!")

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} isn't valid.")
    num = int(input("Enter a number between 1 and 10: "))

print(f"Your number is {num}.")