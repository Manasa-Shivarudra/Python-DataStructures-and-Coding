## Remove a Given Character from a String:

#Time Complexity: O(n)
#Space Complexity: O(1)

str = 'manasa'
char_rem = input("Enter the given character to be removed: ")

def remooveGivenChar(str, char_rem):
    ip_str = list(str)
    i=0
    while i<len(ip_str):
        if ip_str[i] == char_rem:
            ip_str.pop(i)
            break
        else:
            i+=1
    ip_str = ''.join(ip_str)
    return ip_str

op_str = remooveGivenChar(str, char_rem)
print("String after removing the given character:", op_str)

