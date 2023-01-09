    #Python program to calculate sum of integers in string.

str1 = input("Enter the appropriate string: ")
sum = 0

for i in str1:
        if i.isdigit():
            sum = sum + int(i)
print(f"Sum is: {sum}")


