positive_integer = int(input("Please enter a positive integer: "))
print("The factors of ", positive_integer, "are:")
for factor in range(1, positive_integer+1):
    if positive_integer % factor == 0:
        print(factor)
