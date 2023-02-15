## Remove duplicate characters in a given string:

#Space Complexity: O(n)
# Time Complexity: O(n)
import sys

str = 'aabbccddddmans'

def removeAllDuplicateChars(str):
    ip_str = list(str)
    count = {}
    for i in ip_str:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    i=0
    while i < len(ip_str):
        if count[ip_str[i]]>1:
            ip_str.pop(i)
        else:
            i += 1
    ip_str = ''.join(ip_str)
    return ip_str

rem_dup = removeAllDuplicateChars(str)
print(rem_dup)