#Python program to replace the string space with a given character.

char1 = input("Enter a string")
replace_char = input("Input the replacement character")

final_str = char1.replace(" ", replace_char)
print(f"The string after replacing: {final_str}")