## Program to Seggregare 0's, 1's and 2's

#using inbuilt sort method
# space complexity = o(1)
#Time complexity = O(n log n)

arr = [1,2,1,2,0,1,0,2,0]

def Seggregate10and2sort(arr):
    arr.sort()

Seggregate10and2sort(arr)
print("Seggregating 0's, 1's and 2's using sort method: ", arr)

arr1 = [2,1,1,2,1,2,0,1,0,2,0]

#Space compexity = O(1)
#Time Complexity = O(n)
def Seggregate01and2Inplace(arr):
    count0 = 0
    count1 = 0
    for i in arr:
        if i==0:
            count0+=1
        elif i==1:
            count1+=1
    for i in range(0,count0):
        arr[i] =0
    for i in range(count0, count0+count1):
        arr[i]=1
    for i in range(count0+count1, len(arr)):
        arr[i] =2
    return arr

Seggregate01and2Inplace(arr1)
print("Seggregation of 0's, 1's and 2's using inplace: ", arr1)

## Seggrating 0, 1 and 2 using Dutch National Flag Algorithm
#Space compexity = O(1)
#Time Complexity = O(n)

def Segrregate01and2DNFA(arr):
    lo = 0
    mid = 0
    hi = len(arr)-1

    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo+=1
            mid+=1
        elif arr[mid] ==1:
            mid+=1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi-=1
    return arr

arr2=[2,1,2,0,0,1,0,2,1,0]
Segrregate01and2DNFA(arr2)
print("Seggregation of 0's, 1's and 2's using DNFA: ", arr2)




