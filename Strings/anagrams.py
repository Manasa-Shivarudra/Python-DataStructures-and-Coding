#Python Program to check if two Strings are Anagram.

str1 = input("Enter string1")
str2 = input("Enter string2")

str1 = str1.lower()
str2 = str2.lower()

if len(str1) == len(str2):
    sortedstr1 = sorted(str1)
    sortedstr2 = sorted(str2)

    if(sortedstr1 == sortedstr2):
        print("Strings are Anagrams")
    else:
        print("Strings are not Anagrams")