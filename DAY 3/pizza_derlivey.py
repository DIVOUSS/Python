print("\033[1;4mWelcome to Python Deliveries.\nBest Pizza in town\033[0m")

size = input("What size of pizza do you want \033[1mS $15 / M $20 / L $25\033[0m: ").strip().lower()
extra_paneer = input("Would you like extra panner \033[1m+$2 for S and +$3 for M/L\033[0m on that 😋😋 (Yes or No): ").strip().lower()
cheese_burst = input("What about cheese burst \033[1m+$1\033[0m 🍕🧀🧀 (Yes or No): ").strip().lower()
bill = 0

if size in ('small' , 's'):
    bill += 15
elif size in ('medium' , 'm'):
    bill += 20 
elif size in ('large' , 'l'):
    bill += 25
else:
    print("Invalid size entered. Defaulting to Small.")
    bill += 15

if extra_paneer in ('yes' , 'y'):
    if size in ('small' , 's'):
        bill += 2
    else:
        bill += 3

if cheese_burst in ('yes' , 'y'):
    bill += 1

print(f"Please pay ${bill} at the counter.\nCome again")