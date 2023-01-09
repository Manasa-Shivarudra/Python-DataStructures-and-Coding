#Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.

mystr = input("Enter a string:")
vowels = ('a','e','i','o','u')
res= ""

for ch in mystr:
    if ch in vowels:
        res = mystr.replace(ch, '-', 1)
        break
print(f"The resultant string after replacing first vowel with - is {res}")