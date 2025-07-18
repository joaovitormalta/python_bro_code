# file_path = "stuff/output.txt"

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file doesn't exists")
# except PermissionError:
#     print("You don't have permission to read this file")

# import json

# file_path = "stuff/output.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content["name"])
#         print(content["age"])
#         print(content["job"])
# except FileNotFoundError:
#     print("That file doesn't exists")
# except PermissionError:
#     print("You don't have permission to read this file")

import csv

file_path = "stuff/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("That file doesn't exists")
except PermissionError:
    print("You don't have permission to read this file")