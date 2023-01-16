import sys

## Space Complexity is O(1)
## Time Complexity is O(n)

def min(arr):
    #check if the array is empty
    if len(arr) == 0:
        minElement = -1
    else:
        minElement = sys.maxsize
        for i in arr:
            if i < minElement:
                minElement = i
    return minElement

def max(arr):
    #check if the array is empty
    if len(arr) == 0:
        maxElement = -1
    else:
        maxElement = -sys.maxsize
        for i in arr:
            if i > maxElement:
                maxElement = i
    return maxElement

arr = [78,81,1,3,4,0]
minEle = min(arr)
maxEle = max(arr)
print(f'The minimum of given array is {minEle}')
print(f'The maximum of given array is {maxEle}')
