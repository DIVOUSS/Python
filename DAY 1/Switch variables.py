glass1 = input("What does 1st glass have?\n")
glass2 = input("What does 2nd glass have?\n")
print("before " + glass1 + glass2)

glass = glass1
glass1 = glass2
glass2 = glass

print("After " + glass1 + glass2)