## Find the unique element in an Array
import sys

# Space complexity : O(n)
# Time complexity : O(n)

arr = [0,1,7,7,5,5,2,2,9,9]
def uniqueEelemnt1(arr):
    count = {}
    for i in arr:
            count[i] = True

    ans = []

    for key, value in count.items():
        ans.append(key)
    return ans

unique = uniqueEelemnt1(arr)
print("Unique Elements in arr: ", unique)

def uniqueEelemnt2(arr):
    count = {}
    for i in arr:
        count[i] = True
    ans = list(count.keys())
    return ans

unique2 = uniqueEelemnt2(arr)
print("Unique element in arr: ", unique2)

# Space complexity : O(1)
# Time complexity : O(1)
def uniqueEelemntusingSet(arr):
    return list(set(arr))

unique3 = uniqueEelemntusingSet(arr)
print("Unique element in arr: ", unique3)