# doubles = [x * 2 for x in range(1, 11)]

# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)

# triples = [y * 3 for y in range(1, 11)]

# print(triples)

# squares = [z**2 for z in range(1, 11)]

# print(squares)

# fruits = ['apple', 'banana', 'cherry', 'date']
# uppercase_fruits = [fruit.upper() for fruit in fruits]

# print(uppercase_fruits)

# first_letters = [fruit[0] for fruit in fruits]
# print(first_letters)

# numbers = [1, -2, 3, -4, 5, -6]
# positive_numbers = [num for num in numbers if num >= 0]
# print(positive_numbers)
# negative_numbers = [num for num in numbers if num < 0]
# print(negative_numbers)
# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)
# odd_numbers = [num for num in numbers if num % 2 != 0]
# print(odd_numbers)

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)