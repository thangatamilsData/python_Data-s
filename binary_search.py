def binary_search(arr, target):
    low = 0
    high = len(arr)
    while low  <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

array = [1, 2, 22, 35, 45, 55, 66, 77, 88, 99, 100]
target = 77

binary = binary_search(array,target)

print(f"the index is {binary}")
