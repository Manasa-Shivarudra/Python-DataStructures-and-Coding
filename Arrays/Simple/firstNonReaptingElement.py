## Find the first non repeating element in an Array
import sys

# Space complexity : O(n)
# Time complexity : O(n)

arr = [0,1,1,7,7,5,5,2,2,9,9]
def firstNonRepeatingEelemnt1(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    ans = []

    for num, cou in count.items():
        if cou ==1:
            ans.append(num)

    if len(ans) > 0:
        return ans[0]
    return -1

nonRepeat = firstNonRepeatingEelemnt1(arr)
print("Non Repeating element in arr: ", nonRepeat)

def firstNonRepeatingEelemnt2(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    ans = -1

    for num, cou in count.items():
        if cou ==1:
            ans = num
            break
    return ans

nonRepeat2 = firstNonRepeatingEelemnt2(arr)
print("Non Repeating element in arr: ", nonRepeat2)