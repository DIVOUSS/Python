weight = float(input("Please enter your weight in  kg: "))
height = float(input("Please enter your height in in meters: "))

BMI = weight / (height ** 2)

print("Your BMI is: " + str(BMI))

print("Your BMI is: %.2f" % BMI)

print("Your BMI is: " + str(round(BMI)))

print("Your BMI is: " + str(round(BMI, 2)))

print(f"Your BMI is: {BMI:.2f}")

if BMI < 18.5:
    print(f"{BMI:.2f} means you are malnourished.\nPlease take care if yourself.")
elif BMI < 24.9:
    print(f"{BMI:.2f} means you are healthy.\nKeep up the good work")
else:
    print(f"{BMI:.2f} means you are overweight.\nKindly change your diet.")