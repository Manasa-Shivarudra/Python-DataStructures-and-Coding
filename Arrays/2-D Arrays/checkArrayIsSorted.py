## Check if the given array is sorted

## Space complexity: O(n)
## Time complexity: O(n)

arr1 = [1,2,5,7,8]
arr2 = [2,1,3,7,4]

## Recurrsion: ## chopping the element from beginning of array
def sortedOrNot(arr):
    if len(arr)==0 or len(arr)==1:
        return True
    return arr[0]<arr[1] and sortedOrNot(arr[1:])

flag1 = sortedOrNot(arr1)
print(flag1)

flag2 = sortedOrNot(arr2)
print(flag2)

## Space complexity: O(n)
## Time complexity: O(n)
## chopping the end from end of array
def sortedOrNot2(arr):
    n= len(arr)
    if len(arr)==0 or len(arr)==1:
        return True
    return arr[n-2]<arr[n-1] and sortedOrNot2(arr[0:n-1])

flag1 = sortedOrNot2(arr1)
print(flag1)

flag2 = sortedOrNot2(arr2)
print(flag2)

## Iterative approach:
## Space complexity: O(1)
## Time complexity: O(n)

def sortedOrNotIterative(arr):
    if len(arr) == 0 or len(arr)==1:
       return True
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
           return False
    return True

iterFlag1 = sortedOrNotIterative(arr1)
print(iterFlag1)

iterFlag2 = sortedOrNotIterative(arr2)
print(iterFlag2)