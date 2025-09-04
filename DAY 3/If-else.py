print("\nWelcome to the rollercoaster!!!!!")

height = int(input(f"Please enter your Height in cm:"))

if height > 120:
    age = int(input(f"Please enter your AGE:"))
    if age > 18:
        print(f"Kindly pay \033[1m$12\033[0m at the counter.\nEnjoy your ride and don't forget to fasten your seatbelt.")
    elif age >= 12 and age <= 18:
        print(f"Kindly pay \033[1m$7\033[0m at the counter.\nEnjoy your ride and don't forget to fasten your seatbelt.")
    else:
        print(f"Kindly pay \033[1m$5\033[0m at the counter.\nEnjoy your ride and don't forget to fasten your seatbelt.")
else:
    print(f"We are very sorry you can't enter, Try again next year......")