## Program to Seggregate 0's and 1's in an array
## Time Complexity - O(nlogn)
## Space complexity = O(1)

def seggregate0And1(arr):
    arr.sort()

arr = [1,0,1,1,0,1,0]
seggregate0And1(arr)
print(arr)

##Optimized program to Seggregate 0's and 1's in an array
# Time complexity - O(n)
# Space complexity = O(1)

def optSeggregate0And1(arr):
    count = 0
    for i in arr:
        if i == 0:
            count +=1
    for i in range(count):
        arr[i] = 0
    for i in range(count,len(arr)):
        arr[i] = 1

arr = [1,0,1,1,0,1,0]
optSeggregate0And1(arr)
print(f"Optimized Seggregation of 0's and 1's {arr}")

##while program to Seggregate 0's and 1's in an array
# Time complexity - O(n)
# Space complexity = O(1)

def whileSeggregation0And1(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        while arr[left] == 0 and left<right:
            left += 1
        while arr[right] == 1 and left<right:
            right -= 1
        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1

arr = [1,0,1,1,0,1,0]
whileSeggregation0And1(arr)
print(f"While Seggregation of 0's and 1's {arr}")


##2 pointer to Seggregate 0's and 1's in an array
# Time complexity - O(n)
# Space complexity = O(1)

def twoPointerSeggragate0And1(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        if arr[left] == 1:
            arr[left], arr[right] = arr[right], arr[left]
            right-=1
        else:
            left+=1

arr = [1,0,1,1,0,1,0]
twoPointerSeggragate0And1(arr)
print(f"2 pointer Seggregation of 0's and 1's {arr}")