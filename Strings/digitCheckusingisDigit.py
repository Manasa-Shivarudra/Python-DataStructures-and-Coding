##Python program to check given character is digit or not using isdigit() method

char1 = input("Enter a character to check if it is a digit")

if char1.isdigit():
    print(f"The given character {char1} is a digit")
else:
    print(f"The given character {char1} is not a digit")