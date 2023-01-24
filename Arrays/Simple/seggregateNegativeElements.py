## Move negative elements to one side of the array

# Space complexity : O(1)
# Time complexity : O(n)
def seggregateNegativeElements1(arr):
     i = 0
     j = len(arr)-1
     while i < j:
         if arr[i] < 0:
             arr[i], arr[j] = arr[j], arr[i]
             j-=1
         else:
            i+=1

arr1= [1,2,-3,-500,9]
seggregateNegativeElements1(arr1)
print("Array is sroted: ", arr1)


#maintains the order of the array
# Space complexity : O(1)
# Time complexity : O(n)
def seggregateNegativeElements2(arr):
    i = 0
    alpha=[]
    while i < len(arr):
        if arr[i] < 0:
           alpha.append(arr[i])
           arr.pop(i)
        else:
            i+=1
    for i in alpha:
        arr.append(i)

arr2 = [1, 2, -3, -500, 9, -10, -1]
seggregateNegativeElements2(arr2)
print("Array is sroted: ", arr2)