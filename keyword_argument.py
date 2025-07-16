# def hello(greeting, title, f_name, l_name):
#     print(f"{greeting} {title}{f_name} {l_name}!")

# hello("Hello", "Mr.", "Spongebob", "Squarepants")
# hello(greeting="Hello", title="Mr.", f_name="Spongebob", l_name="Squarepants")

# for x in range(11):
#     print(x, end=" ")

# print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=55, area=24, first=99828, last=5946)
print(phone_num)