## Remove a Given Character from a String:

#Time Complexity: O(n)
#Space Complexity: O(1)

str = 'abbbaaaaccccdddd'
char_rem = input("Enter the given character to be removed: ")

def removeAllGivenChar(str, char_rem):
    ip_str = list(str)
    i=0
    while i<len(ip_str):
        if ip_str[i] == char_rem:
            ip_str.pop(i)
        else:
            i+=1
    ip_str = ''.join(ip_str)
    return ip_str

op_str = removeAllGivenChar(str, char_rem)
print("String after removing the given character:", op_str)

