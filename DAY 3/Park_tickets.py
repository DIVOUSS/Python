print("🎢 Welcome to the Rollercoaster!!! 🎢")
height = int(input(f"Please Enter your Height in cm: "))
ticket_price = 0

if height < 120:
    print(f"A tad short my friend.Try again next year......")
else:
    age = int(input(f"Please enter your age: "))

    #People from 45-55 generally go from midlife crisis.
    if 45 <= age <= 55:
        print("You don'd need to pay anything my friend, Hope this ride makes you feel better.")
    else:
        if age < 12:
            ticket_price= 5
            print(f"Child Tickets are \033[1m$5\033[0m.")
        elif age <=18:
            ticket_price= 7
            print(f"Youth Tickets are \033[1m$7\033[0m.")        
        else:
            ticket_price= 12
            print(f"Adult Tickets are \033[1m$12\033[0m.")
        

    photo = input(f"Would you like a Photo to remember this memory(y/n): ").strip().lower()
    if photo in ('y,yes'):
        ticket_price += 3
        
    print(f"Kindly pay \033[1m${ticket_price}\033[0m at the counter.\nEnjoy your ride and don't forget to fasten your seatbelt.")