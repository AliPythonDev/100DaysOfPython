# year = int(input("Which year do you want to check for a Leap Year? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year}, is a Leap Year")
#         else:
#             print(f"{year}, is not a Leap Year.")
#     else:
#         print(f"{year}, is a Leap Year.")
# else:
#     print(f"{year}, is not a Leap Year.")
# To improve readability and avoid unnecessary indentation, we can simplify it a bit:
year = int(input("Which year do you want to check for a Leap Year? "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")
