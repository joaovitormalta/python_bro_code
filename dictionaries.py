capitals = {
    "USA": "Washington D.C",
    "India": "New Dehli",
    "China": "Beijing",
    "Russia": "Moscow"
}

# print(len(capitals))
# print(capitals.get("USA"))

# if capitals.get("Russia"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})

# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys():
#     print(key)

# values = capitals.values()

# for value in capitals.values():
#     print(value)

items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")