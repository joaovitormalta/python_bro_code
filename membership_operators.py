# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter in word:
#     print(f"There is a {letter}!")
# else:
#     print(f"{letter} was not found!")

# if letter not in word:
#     print(f"{letter} was not found!")
# else:
#     print(f"There is a {letter}!")

# students = {"Spongebob", "Patrick", "Squidward"}

# student = input("Enter a student name: ")

# if student in students:
#     print(f"{student} is a student.")
# else:
#     print(f"{student} is not a student.")

# grades = {
#     "Spongebob": "C",
#     "Patrick": "F",
#     "Squidward": "B",
#     "Sandy": "A"
# }

# student = input("Enter a student name: ")

# if student in grades:
#     print(f"{student} has a grade of {grades[student]}.")
# else:
#     print(f"{student} was not found.")

email = "joaovitormaltapinto@gmail.com"

if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address.")