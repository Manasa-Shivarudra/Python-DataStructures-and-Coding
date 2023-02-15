## Reverse a String

#Space Complexity: O(n)
#Time Complexity: O(n)

str1 = 'manasa'

def reverseString(str):
    ip_str = list(str)
    opt_str = '*' * len(str)
    op_str = list(opt_str)
    j =0
    for i in range(len(ip_str)-1,-1,-1):
        op_str[j] = ip_str[i]
        j+=1
    op_str= "".join(op_str)
    print(op_str)

reverseString(str1)

#Space Complexity: O(1)
#Time Complexity: O(n)


def optmizedRevStr(str):
    ip_str = list(str)
    i=0
    j=len(ip_str)-1
    while i<j:
        ip_str[i],ip_str[j] = ip_str[j], ip_str[i]
        i+=1
        j-=1
    ip_str = ''.join(ip_str)
    print(ip_str)

str2 = 'manasa'
optmizedRevStr(str2)