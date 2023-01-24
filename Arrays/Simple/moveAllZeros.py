## Move all Zeroes to end of the array

# Space complexity : O(1)
# Time complexity : O(n)

def moveAllZeros1(arr):
     i = 0
     j = len(arr)-1
     while i < j:
         if arr[i] == 0:
             arr[i], arr[j] = arr[j], arr[i]
             j-=1
         else:
            i+=1

arr1= [0,1,0,2,-3,0,-500,9]
moveAllZeros1(arr1)
print("Array after moving zeros to the End: ", arr1)


#maintains the order of the array
# Space complexity : O(1)
# Time complexity : O(n)
def moveAllZeros2(arr):
    i = 0
    alpha=[]
    while i < len(arr):
        if arr[i] == 0:
           alpha.append(arr[i])
           arr.pop(i)
        else:
            i+=1
    for i in alpha:
        arr.append(i)

arr2= [0,1,0,2,-3,0,-500,9]
moveAllZeros2(arr2)
print("Array after moving zeros to the End with preserving the order of the array: ", arr2)

# Space complexity : O(1)
# Time complexity : O(1) single traversal
def moveAllZeros3(arr):
    i = 0
    for j in range(len(arr)):
        if arr[i] == 0:
           alpha= arr.pop(i)
           arr.append(alpha)
        else:
            i+=1


arr3= [0,1,0,2,-3,0,-500,9]
moveAllZeros2(arr3)
print("Array after moving zeros to the End with preserving the order of the array in single traversal: ", arr3)