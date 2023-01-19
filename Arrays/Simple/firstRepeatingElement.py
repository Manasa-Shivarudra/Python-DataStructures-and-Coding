## Find the first repeating elements in an Array
import sys

# Space complexity : O(n)
# Time complexity : O(n)

arr = [1,2,2,3,3,3,3,4,4,4,5,5,5,6]
def firstRepeatingEelemnt(arr):
    count = {}
    ans=-1
    for i in arr:
        if i not in count:
            count[i] = 1
        else:
            ans=i
            break
    return ans

firstreap = firstRepeatingEelemnt(arr)
print("Duplicate element in arr are: ", firstreap)