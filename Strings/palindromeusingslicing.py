#Python program to check a String is palindrome or not
def isPalindrome(s):
    return s == s[::-1]

str1 = input("Enter the string:")
str1 = str1.lower()
palindrom_check = isPalindrome(str1)

if palindrom_check:
    print(f"{str1} is a Palindrome")
else:
    print(f"{str1} is not a Palindrome")