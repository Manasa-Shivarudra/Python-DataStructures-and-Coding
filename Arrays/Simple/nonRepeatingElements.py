## Find the most frequent element in an Array
import sys

# Space complexity : O(n)
# Time complexity : O(n)

arr = [1,2,2,3,3,3,3,4,4,4,5,5,5,6]
def nonRepeatingEelemnt1(arr):
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
    return ans

nonRepeat = nonRepeatingEelemnt1(arr)
print("Non Repeating element in arr: ", nonRepeat)