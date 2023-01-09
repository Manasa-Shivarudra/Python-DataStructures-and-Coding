#Python program to convert lowercase vowel to uppercase in string.

str1 = input("Enter the string: ")
capitalize_vowel = str1.upper()
vowels = ('a','e','i','o','u')
res = ""

for ch in str1:
    if ch in vowels:
        ch = ch.upper()
    res += ch

print(f"The capitalized string: {res}")