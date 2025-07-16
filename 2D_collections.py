groceries = ({"apple", "orange", "banana", "coconout"},
             {"celery", "carrot", "potato"},
             {"chicken", "fish", "turkey"})

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()