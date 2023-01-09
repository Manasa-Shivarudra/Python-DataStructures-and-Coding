#Python program to copy one string to another string.

str1 = input("Enter string1: ")

str2 = ""

for x in str1:
    str2 = str2 + x
print(f"String2: {str2}")

str3 = str1[:]
print(f"String3: {str3}")

str4 = str1
print(f"String4: {str4}")