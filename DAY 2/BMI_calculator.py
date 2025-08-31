weight = float(input("Please enter your weight in  kg: "))
height = float(input("Please enter your height in in meters: "))

BMI = weight / (height ** 2)

print("Your BMI is: " + str(BMI))

print("Your BMI is: %.2f" % BMI)

print("Your BMI is: " + str(round(BMI)))

print("Your BMI is: " + str(round(BMI, 2)))

print(f"Your BMI is: {BMI:.2f}")