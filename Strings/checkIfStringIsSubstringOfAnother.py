## Check if a string is a substring if another string
## Check if str1 is a substring of str2
#Space Complexity: O(1)
# Time Complexity: O(n^2)

str2 = 'ineuron'
str1 = 'euro'

def isSubstring1(str1,str2):
    m = len(str1)
    n= len(str2)
    for i in range(n-m+1):
        for j in range(m):
            if str2[i+j]!=str1[j]:
                break
        if j+1==m:
            return i
    return -1

flag = isSubstring1(str1,str2)
print(flag)

#Space Complexity: O(1)
# Time Complexity: O(n)
def isSubstring2(str2,str1):
   t=0
   l1 = len(str1)
   i=0
   for i in range(l1):
       if t==len(str2):
           break
       if str1[i]==str2[t]:
           t+=1
       else:
           t=0
   if t<len(str2):
       return -1
   return i-t


flag = isSubstring2(str1,str2)
print(flag)