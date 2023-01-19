## Find the most frequent element in an Array
import sys

# Space complexity : O(n)
# Time complexity : O(n^2)

arr = [1,1,2,2,3,3,3,3,4,4,4,5,5,5]
def mostFrequentElement1(arr):
    count= []
    for i in list(set(arr)):
        c=0
        for j in arr:
            if i == j:
                c+=1
        count.append([i,c])

    max = -sys.maxsize
    ans = -1

    for num, cou in count:
        if cou>max:
            max = cou
            ans = num
    return ans

mostFreq = mostFrequentElement1(arr)
print("Most frequent element in arr: ", mostFreq)

## Using Dictionary
# Space complexity : O(n)
# Time complexity : O(n)

arr2 = [1,1,2,2,3,3,3,3,4,4,4,5,5,5]
def mostFrequentElement2(arr):
    count = {}
    for i in arr:
        if i not in count:
            count[i] =1
        else:
            count[i]+=1
    max = -sys.maxsize
    ans = -1

    for num, cou in count.items():
        if cou > max:
            max = cou
            ans = num
    return ans

mostFreq = mostFrequentElement2(arr2)
print("Most frequent element in arr using dict: ", mostFreq)


