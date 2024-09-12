import time
import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else: 
            high = mid - 1
    return -1
    
arraySizes = [100, 10000, 100000]
for size in arraySizes:
    randomSortedArr = sorted(random.sample(range(size*2), size))
    target = -1

    startTime = time.time()
    linear_search(randomSortedArr, target)
    linearTime = time.time() - startTime

    startTime = time.time()
    binary_search(randomSortedArr, target)
    binaryTime = time.time() - startTime

    print(f"Size: {size}, Linear Time: {linearTime}, Binary Time: {binaryTime}")