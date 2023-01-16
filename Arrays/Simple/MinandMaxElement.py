## Time complexity : O(nlogn)
# space complexity : O(1)

def MinandMax(arr):
    #check if the array is not empty
    if len(arr) == 0:
        minElement = -1
    else:
        arr.sort()
        minElement = arr[0]
        maxElement = arr[-1]

    print(f"Minimum Element of the array is {minElement} \n Maximum Element of the array is {maxElement}")

MinandMax([9,4,6,1,2,45])
