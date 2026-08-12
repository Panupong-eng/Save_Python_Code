number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
if number > 0:
    print(f"{number} is Positive")
elif number < 0:
    print(f"{number} is Negative")
else:
    print(f"{number} is Zero")
if (number > 0) and (number % 2 == 0):
    print("Perfect Even Positive")