# Exercise 2: Shopping Cart

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many items would you like?: "))
total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")