#Python program to print all non repeating character in string.

str1 = input("Enter the string: ")
res = ""

for x in str1:
    count = 0
    for k in str1:
        if x == k:
            count=count+1
            if count > 1:
                break
    if count ==1:
        res += x
print(f"Non Repeating characters: {res}")

#non_repeat = [d for d in ini_list if d['c'] > 10]
