def quick_sort(arr, left = 0, right = None):
    sorted_arr = arr.copy()
    if right is None:
        right = len(sorted_arr) - 1

    if left >= right:
        return sorted_arr

    pivot = partition(sorted_arr, left, right)
    sorted_arr = quick_sort(sorted_arr, left, pivot - 1)
    sorted_arr = quick_sort(sorted_arr, pivot + 1, right)
    return sorted_arr


def partition(arr, left, right):
    pivot = right
    right -= 1
    while left <= right:
        if arr[left] <= arr[pivot]:
            left += 1
        elif arr[right] >= arr[pivot]:
            right -= 1
        else:
            #swaps values
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
    temp = arr[left]
    arr[left] = arr[pivot]
    arr[pivot] = temp
    pivot = left
    return pivot

numbers = [4,3,5,6,1]
print(quick_sort(numbers))
print(quick_sort([1,10,9,5,7,7,8,6]))
