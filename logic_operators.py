# OR
# temp = 25
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled.")
# else:
#     print("The outdoor event is still scheduled.")

#  AND
# temp = 20
# is_sunny = True

# if temp >= 28 and is_sunny:
#     print("It's hot outside!")
#     print("It's sunny!")
# elif temp <= 0 and is_sunny:
#     print("It's cold outside!")
#     print("It's sunny!")
# elif 28 > temp > 0 and is_sunny:
#     print("It's warm outside!")
#     print("It's sunny!")

# NOT
temp = -29
is_sunny = False

if temp >= 28 and not is_sunny:
    print("It's hot outside!")
    print("But it's not sunny!")
elif temp <= 0 and not is_sunny:
    print("It's cold outside!")
    print("But it's not sunny!")
elif 28 > temp > 0 and not is_sunny:
    print("It's warm outside!")
    print("But it's not sunny!")