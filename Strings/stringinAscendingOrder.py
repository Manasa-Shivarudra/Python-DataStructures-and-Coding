#Python Program to sort characters of string in ascending order.

str1 = input("Enter a string: ")
str2 = sorted(str1)
str3 = sorted(str1, reverse=1)

print(f"Ascending string: {str2}")
print(f"Descending string: {str3}")
