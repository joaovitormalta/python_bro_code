from python_poo_car_class import Car

car1 = Car("Mustang", 2025, "red", False)
car2 = Car("Corvette", 2024, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car1.stop()
car1.describe()

print()

print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
car2.drive()
car2.stop()
car2.describe()

print()

print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
car3.drive()
car3.stop()
car3.describe()