## Reverse an Array
# space complexity = o(n)
#Time complexity = O(n)
def reverse1(arr):
    op_arr = [-1] * len(arr)
    j = 0
    for i in range(len(arr)-1, -1,-1):
        op_arr[j] = arr[i]
        j+=1
    return op_arr

arr = [9,8,7,6,5,4,1,2,3]
print("The Reversed array is: ",reverse1(arr))

## 2 pointer approach and inplace reversal
# space complexity = o(1)
#Time complexity = O(n)

def reverse2(arr):
    i = 0
    j = len(arr)-1

    while i<j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    return arr

arr2 = [1,2,3,4,5]
print("The Reversed array is: ",reverse2(arr2))

