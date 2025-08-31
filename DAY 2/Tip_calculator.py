#Taking values
bill = float(input("How much is your bill?\n$"))
tip = float(input("\nHow much would you like to tip?\n%"))
people = float(input("\nHow many people are splitting the bill?\n="))

#Processing them 
amount = (bill + (bill * tip / 100))/people

#Now Viola
print(f"Each should pay : ${amount:.2f}")
