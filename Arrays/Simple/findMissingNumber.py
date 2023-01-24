## Find the missing number in integer array of 1 to 100

import random
def listInt():
    l = []
    for i in range(1, 101):
        l.append(i)
    missingIndex = random.randint(0,99)
    print("Popped Element is : ",l[missingIndex])
    l.pop(missingIndex)
    return l

#Space complexity: O(1)
# Time Complexity: O(n^2)
def findMissingElement1(arr):
    ele = -1
    for i in range(1,101):
        if i not in arr:
            ele = i
            break
    return ele

arr = listInt()
ele = findMissingElement1(arr)
print(f"missing element is: {ele}")

#Space complexity: O(n)
# Time Complexity: O(n)
def findMissingElement2(arr):
    ele = -1
    ins = {}
    for i in arr:
        ins[i] = True
    for i in range(1,101):
        if i not in arr:
            ele = i
            break
    return ele


ele = int(findMissingElement2(arr))
print(f"missing element is: {ele}")

#Space complexity: O(1)
# Time Complexity: O(n)
def findMissingElement3(arr):
    exp_sum = 100*101/2
    actual_sum = 0
    for i in arr:
        actual_sum +=i
    ele = exp_sum - actual_sum
    return ele


ele = int(findMissingElement3(arr))
print(f"missing element is: {ele}")