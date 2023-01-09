mystr = input("Enter a string:")
rmchar = input("Enter the character to removed: ")
removechar = mystr.replace(rmchar, '') #All occurrence of the letter
removefirst = mystr.replace(rmchar, '', 1)
print(removechar)