text_data = "I like Pizza!"

file_path = "stuff/output.txt"

try:
    with open(file=file_path, mode="w") as file:
        file.write(text_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

# file_path = "stuff/output.txt"

# try:
#     with open(file=file_path, mode="w") as file:
#         for employee in employees:
#             file.write(employee + " ")
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists")

# import json

# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "Cook"
# }

# file_path = "stuff/output.json"

# try:
#     with open(file=file_path, mode="w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists")

# import csv

# employees = [
#     ["Name", "Age", "Job"],
#     ["Spongebob", 30, "Cook"],
#     ["Patrick", 37, "Unemployed"],
#     ["Sandy", 27, "Scientist"]
# ]

# file_path = "stuff/output.csv"

# try:
#     with open(file=file_path, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists")