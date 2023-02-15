## Find the maximum occurring character in a given string

# Time complexity - O(n^2)
# Space Complexity - O(n)
import sys

str = 'manasa'

def maxOccurChar(str):
    count=[]
    for i in list(set(str)):
        c=0
        for j in str:
            if i==j:
                c+=1
        count.append([i,c])

    max = -sys.maxsize
    ans = ''
    for char,cou in count:
        if cou > max:
            max = cou
            ans = char

    return ans

maxocc = maxOccurChar(str)
print(maxocc)

# Time complexity - O(n)
# Space Complexity - O(n)
def maxOccuringChar(str):
    count = {}
    for i in str:
        if i not in count:
            count[i]=1
        else:
            count[i] +=1

    max = -sys.maxsize
    ans = ''
    for item, cou in count.items():
        if cou > max:
            max = cou
            ans = item
    return ans

max = maxOccuringChar(str)
print(max)
