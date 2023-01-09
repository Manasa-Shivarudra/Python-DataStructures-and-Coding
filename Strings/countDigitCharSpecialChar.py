#Python program to count alphabets, digits and special characters.

str1 = input("Enter the string: ")
digit_count = 0
spchar_count = 0
char_count = 0

for ch in str1:
    if ch.isdigit():
        digit_count = digit_count+1
    elif ch.isalpha():
        char_count += 1
    else:
        spchar_count += 1

print(f"The digit Count is: {digit_count}")
print(f"The char Count is: {char_count}")
print(f"The special char Count is: {spchar_count}")