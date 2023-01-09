# Python Program to count occurrence of a given characters in string

mystr = input("Enter the string")
givenChar = input("Enter the character")
count = 0
for i in range(0, len(mystr)):
    if mystr[i] == givenChar:
        count = count + 1
print("Count of character:",count)