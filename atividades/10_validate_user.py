# Exercise 10: Validate User Input

username = input("Enter your username: ")

if len(username) > 12:
    print("Username must be less than 12 characters.")
elif username.find(" ") != -1:
    print("Username must not contain spaces.")
elif not username.isalpha():
    print("Username must contain only letters.")
else:
    print(f"Welcome, {username}!")