# def day_of_week(day):
#     match day:
#         case 1:
#             return "Monday"
#         case 2:
#             return "Tuesday"
#         case 3:
#             return "Wednesday"
#         case 4:
#             return "Thursday"
#         case 5:
#             return "Friday"
#         case 6:
#             return "Saturday"
#         case 7:
#             return "Sunday"
#         case _:
#             return "Invalid day number"
        
# print(day_of_week(3))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
        
print(is_weekend("Sunday"))  
print(is_weekend("Monday"))
print(is_weekend("Friday"))
print(is_weekend("Funday"))

set1 = {1, 2, 3}
intersection_set = set1.intersection()