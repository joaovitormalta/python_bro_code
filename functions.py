# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print(f"Happy birthday to {name}!")
#     print()

# happy_birthday("João", 20)
# happy_birthday("Hannah", 50)
# happy_birthday("Pedro", 65)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}!")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("João", 42.50, "01/01")

# Return

# def add(a, b):
#     z = a + b
#     return z

# def subtract(a, b):
#     z = a - b
#     return z

# def multiply(a, b):
#     z = a * b
#     return z

# def divide(a, b):
#     z = a // b
#     return z

# z = add(1, 2)
# print(z)

# z = subtract(5, 3)
# print(z)

# z = multiply(6, 3)
# print(z)

# z = divide(9, 3)
# print(z)

def create_full_name(f_name, l_name):
    f_name = f_name.capitalize()
    l_name = l_name.capitalize()

    full_name = f_name + " " + l_name
    return full_name

full_name = create_full_name("spongebob", "squarepants")
print(full_name)