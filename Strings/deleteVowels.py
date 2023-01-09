#Python program to delete vowels in a given string.

str1 = input("Enter the string: ")
vowels = ('a','e','i','o','u')
res = ""

for ch in str1:
    if ch in vowels:
        ch = ''
    res += ch

print(f"The result string after deleting vowels: {res}")

