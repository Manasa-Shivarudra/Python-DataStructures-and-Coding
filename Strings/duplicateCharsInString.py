## Print the duplicate characters in a Given String

#Space Complexity: O(n)
# Time Complexity: O(n)
import sys

str = 'aabbccddddmans'

def duplicatechars(str):
    ip_str = list(str)
    count = {}
    for i in ip_str:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1

    ans = []

    for item, cnt in count.items():
        if cnt>1:
            ans.append(item)
    return ans

dupele = duplicatechars(str)
print(dupele)