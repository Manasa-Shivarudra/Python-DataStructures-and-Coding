## Remove Duplicate Elements from the array

## Space complexity: O(1)
## Time complexity: O(n)

arr1 = [1,7,7,2,2,9]

def removeDuplicateElements(arr):
    inst = {}
    i=0
    while i<len(arr):
        if arr[i] in inst:
            arr.pop(i)
        else:
            inst[arr[i]] =1
            i+=1

removeDuplicateElements(arr1)
print("Array after deletion of duplicates: ", arr1)
