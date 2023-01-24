## Check if the given array is sorted or not

# Space complexity : O(n)
# Time complexity : O(n)
# Recurrsive Approach
def sortedOrNot1(arr):
    if len(arr) ==0 or len(arr)==1:
        return True
    return arr[0]<arr[1] and sortedOrNot1(arr[1:])

arr1= [1,2,3,9]
flag = sortedOrNot1(arr1)
print(f"Array is sroted: {flag}")

# Space complexity : O(n)
# Time complexity : O(n)
def sortedOrNot2(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    return arr[n-1] < arr[n-2] and sortedOrNot2(arr[0:n-1])

arr2= [1,2,3,500,9]
flag = sortedOrNot2(arr2)
print(f"Array is sroted: {flag}")

# Space complexity : O(1)
# Time complexity : O(n)
# Iterative Approach
def sortedOrNot3(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return True
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

arr3= [1,2,3,500,9]
flag = sortedOrNot3(arr3)
print(f"Array is sroted: {flag}")
