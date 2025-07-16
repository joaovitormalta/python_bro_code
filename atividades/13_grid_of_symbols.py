# Exercise 13: Grid of Symbols

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(0, rows):
    for y in range(0, columns):
        print(symbol, end="")
    print()