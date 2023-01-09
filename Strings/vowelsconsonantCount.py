#Python program to count Occurrence Of Vowels & Consonants in a String.

str1 = input("Enter the string")
str1 = str1.lower()
vowels = ('a','e','i','o','u')
consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't','v', 'w', 'x', 'y', 'z')
vowel_count = 0
cons_count = 0

for ch in str1:
    if ch in vowels:
        vowel_count = vowel_count+1
    elif ch in consonants:
        cons_count += 1
    else:
        None

print(f"The vowel Count is: {vowel_count}")
print(f"The consonant Count is: {cons_count}")