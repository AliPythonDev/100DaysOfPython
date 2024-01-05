print("Welcome to the Roller Coaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the Roller Coaster")
    age = int(input("What is your Age? "))
    if age < 12:
        bill = 5
        print("Child Tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth Tickets are $7.")
    else:
        bill = 12
        print("Adult Tickets are $12.")

wants_photo = input("Do you want a Photo taken? Y or N. ")
if wants_photo == 'Y':
    bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")