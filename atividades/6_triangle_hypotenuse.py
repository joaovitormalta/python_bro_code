# Exercise 6: Triangle Hypotenuse
import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
hypotenuse = math.hypot(a, b)

print(f"The hypotenuse of the triangle is: {round(hypotenuse, 2)}cm")