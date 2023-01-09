#Python program to check given character is vowel or consonant.

char1 = input("Enter the Character")
char1 = char1.lower()
vowels = ('a','e','i','o','u')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't','v', 'w', 'x', 'y', 'z')

if char1 in vowels:
    print(f"The given character {char1} is a vowel")
elif char1 in consonants:
    print(f"The given character {char1} is a consonant")
else:
    print(f"The given character {char1} is neither a vowel nor a consonant")