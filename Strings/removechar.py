my_string = input('Input String:')
char_to_remove = input('Enter the character to be removed')
res_string = ""

for i in range(0, len(my_string)):
    if my_string[i] != char_to_remove:
        res_string = res_string + my_string[i]
print(res_string)
