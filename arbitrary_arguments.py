# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4, 5))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Senhor", "João", "Vitor", "Malta", "Pinto", "Terceiro")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(
#     street="Rua José Claro da Silva",
#     apt="100",
#     city="Volta Redonda",
#     state="RJ",
#     zip="27213-120"
#     )

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs.keys():
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs.keys():
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Senhor", "João", "Vitor", "Malta", "Pinto",
               street="123 Fake St.",
               pobox="Po box 1001",
               city="Detroit",
               state="Mi",
               zip="54321")