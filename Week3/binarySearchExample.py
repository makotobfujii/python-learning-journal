def binary_search(arr, target):
    low = 0 
    high = len(arr) - 1

    while low <= high: 
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target: 
            low = mid + 1
        else:
            high = mid - 1

    return - 1

def main():
    array = [10, 11, 15, 23, 45, 70]
    search = 70
    print(binary_search(array, search))

