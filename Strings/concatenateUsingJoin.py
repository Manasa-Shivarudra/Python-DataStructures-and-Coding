#Python program to concatenate two strings using join() method.

str1 = input('Enter first string: ')
str2 = input('Enter second string: ')
#printing the output after using join() method
print("String after concatenation :"," ".join([str1, str2]))

##Python program to concatenate two strings without using join() method.
str3 = str1 + " " + str2
print(f"String after concatenation : {str3}")