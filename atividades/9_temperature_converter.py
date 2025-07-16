# Exercise 9: Temperature Converter

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature = (temperature * 9/5) + 32
    unit = "F"
    print(f"The temperature is {round(temperature)}°{unit}.")
elif unit == "F":
    temperature = (temperature - 32) * 5/9
    unit = "C"
    print(f"The temperature is {round(temperature)}°{unit}.")
else:
    print(f"{unit} was not valid")

