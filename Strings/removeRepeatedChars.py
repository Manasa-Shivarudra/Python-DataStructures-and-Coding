#Python program to remove repeated character from string.

str1 = input("Enter the string: ")
str1 = str1.lower()
res = ""

for ch in str1:
    if ch not in res:
        res = res + ch

print(f"The result string is: {res}")