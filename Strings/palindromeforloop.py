#Python program to check a String is palindrome or not
str1 = input("Enter a string")
str1 = str1.lower().replace(" ", "")
rev_str1 = ""

for i in range(len(str1)-1, -1, -1):
    rev_str1 += str1[i]

if rev_str1 == str1:
    print(f"{str1} is a Palindrome")
else:
    print(f"{str1} is not a Palindrome")