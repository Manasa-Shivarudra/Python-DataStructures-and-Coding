#Python program to separate characters in a given string.

string = input("Enter a String: ")
string = string.replace(" ", "")
letter = [x for x in string]
print(letter)
#lst = []
#for letter in string:
   # lst.append(letter)
#print(lst)